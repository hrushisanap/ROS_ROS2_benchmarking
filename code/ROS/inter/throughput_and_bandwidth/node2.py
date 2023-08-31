#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def topic1_callback(msg):
    rospy.loginfo("1")
    
    topic2_publisher.publish("0")
    rospy.loginfo("0")

def node2_subscriber_publisher():
    rospy.init_node('node2_subscriber_publisher', anonymous=True)
    rospy.Subscriber('topic1', String, topic1_callback)

    global topic2_publisher
    topic2_publisher = rospy.Publisher('topic2', String, queue_size=50000)
    rospy.spin()

if __name__ == '__main__':
    try:
        node2_subscriber_publisher()
    except rospy.ROSInterruptException:
        pass
