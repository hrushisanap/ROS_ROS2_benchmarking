#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def topic2_callback(msg):
    rospy.loginfo("1")

def node3_subscriber():
    rospy.init_node('node3_subscriber', anonymous=True)
    rospy.Subscriber('topic2', String, topic2_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        node3_subscriber()
    except rospy.ROSInterruptException:
        pass
