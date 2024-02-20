#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from serial import Serial

def arduino_callback(data):
    rospy.loginfo("Arduino says: %s", data.data)

def listener():
    rospy.init_node('arduino_listener', anonymous=True)
    rospy.Subscriber('chatter', String, arduino_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        ser = Serial('/dev/ttyUSB0', 115200) # กำหนดพอร์ตและ Baudrate ของ Arduino
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('arduino_publisher', anonymous=True)
        rate = rospy.Rate(10) # 10 Hz
        while not rospy.is_shutdown():
            if ser.in_waiting > 0:
                data_str = ser.readline().strip()
                rospy.loginfo("Received from Arduino: %s", data_str)
                pub.publish(data_str)
                rate.sleep()
    except rospy.ROSInterruptException:
        pass


