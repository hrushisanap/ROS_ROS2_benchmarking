#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def publisher(hz):
    rospy.init_node('publisher_node', anonymous=True)
    pub = rospy.Publisher('topicthroughput', String, queue_size=10000)
    rate = rospy.Rate(hz)
    message_size_kb = 50
    msg = 'a' * message_size_kb * 1024
    start_time = rospy.get_time()
    while not rospy.is_shutdown() and (rospy.get_time() - start_time) <60:
        pub.publish(f"{hz} {msg}")
        rospy.loginfo(f"{hz}")
        rate.sleep()

if __name__ == '__main__':
    try:
        frequencies = [i for i in range(10,201,10)]
        for hz in frequencies:
            publisher(hz)
            rospy.sleep(10.)
    except rospy.ROSInterruptException:
        pass