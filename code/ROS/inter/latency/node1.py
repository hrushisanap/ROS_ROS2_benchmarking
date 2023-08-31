#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def shutdown_node():
    rospy.signal_shutdown("Shutdown Requested")

def node1_publisher():
    topic1_publisher = rospy.Publisher('topic1', String, queue_size=50000)
    rospy.init_node('node1_publisher', anonymous=True)
    sizes = [i for i in range(10, 201, 10)]
    frequencies= [i for i in range(10, 201, 10)]

    while not rospy.is_shutdown():
        for i in sizes:
            msg = "a" * 1024 * i
            for j in frequencies:
                rate =rospy.Rate(j)
                for k in range(1500):
                    topic1_publisher.publish(msg)
                    rospy.loginfo(f"{i},{j},{k}")
                    rate.sleep()
                rospy.sleep(15.0)
            rospy.sleep(15.0)
        shutdown_node()

if __name__ == '__main__':
    try:
        node1_publisher()
    except rospy.ROSInterruptException:
        pass
