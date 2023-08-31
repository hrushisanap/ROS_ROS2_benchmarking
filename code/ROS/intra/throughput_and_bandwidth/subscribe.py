#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data[0:3])

def subscriber():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('topicthroughput', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()