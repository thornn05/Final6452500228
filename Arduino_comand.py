#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool


def button_callback(data):
    rospy.loginfo("NodeHandle nh: %s", data.data)

def listener():
    rospy.init_node('arduino_listener', anonymous=True)
    rospy.Subscriber("NodeHandle nh", Bool, button_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

