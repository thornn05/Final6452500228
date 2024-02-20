#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

# Parameter for Default Scale
# ...

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x300")

LED_TOPIC = "led_control"

# Initial ROS node and determine Publish or Subscribe action
# ...

rospy.init_node("Remote")
pub1 = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
pub2 = rospy.Publisher("command", String, queue_size=10)
led_pub = rospy.Publisher(LED_TOPIC, String, queue_size=10)
def fw():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = 0.0
    pub1.publish(cmd)
    pub2.publish("Forward")

def bw():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z = 0.0
    pub1.publish(cmd)
    pub2.publish("Backward")

def lt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = AngularVel.get()
    pub1.publish(cmd)
    pub2.publish("Left turn")

def rt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = -AngularVel.get()
    pub1.publish(cmd)
    pub2.publish("Right turn")

def pen_on():
    # Publish a command to ROS to turn on the pen
    pub2.publish("PenOn")
    # Assuming you have a way to send a signal to Arduino to turn on the LED
    # You may need additional code here to handle the Arduino communication
    turn_on_led()

def pen_off():
    # Publish a command to ROS to turn off the pen
    pub2.publish("PenOff")
    # Assuming you have a way to send a signal to Arduino to turn off the LED
    # You may need additional code here to handle the Arduino communication
    turn_off_led()

LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1)  # 1 is default value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1)  # 1 is default value for scale
AngularVel.pack()

B1 = Button(text="Forward", command=fw)
B1.place(x=73, y=120)

B2 = Button(text="Backward", command=bw)
B2.place(x=73, y=230)

B3 = Button(text="Turn Left", command=lt)
B3.place(x=20, y=180)

B4 = Button(text="Turn Right", command=rt)
B4.place(x=128, y=180)

# Add a button for turning on the pen
B5 = Button(text="PenOn", command=pen_on)
B5.place(x=20, y=300)

# Add a button for turning off the pen
B6 = Button(text="PenOff", command=pen_off)
B6.place(x=128, y=300)

frame.mainloop()


