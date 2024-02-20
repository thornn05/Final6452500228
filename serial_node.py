#include <ros.h>
#include <std_msgs/Bool.h>

const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int buttonPin3 = 4;
const int ledPin13 = 13;
const int ledPin5 = 5;

int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;

ros::NodeHandle nh;

std_msgs::Bool led_msg;

ros::Publisher pub_led("led_status", &led_msg);

void setup() {
  nh.initNode(serial);
  nh.advertise(pub_led);
  
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(ledPin13, OUTPUT);
  pinMode(ledPin5, OUTPUT);
}

void loop() {
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);

  if (buttonState1 == HIGH) {
    digitalWrite(ledPin13, HIGH);
    led_msg.data = true;
    pub_led.publish(&led_msg);
  } else {
    digitalWrite(ledPin13, LOW);
    led_msg.data = false;
    pub_led.publish(&led_msg);
  }

  if (buttonState2 == HIGH) {
    digitalWrite(ledPin5, HIGH);
  } else {
    digitalWrite(ledPin5, LOW);
  }

  if (buttonState3 == HIGH) {
    digitalWrite(ledPin13, HIGH);
    digitalWrite(ledPin5, HIGH);
  } else {
    digitalWrite(ledPin13, LOW);
    digitalWrite(ledPin5, LOW);
  }

  nh.spinOnce();
  delay(100);
}
