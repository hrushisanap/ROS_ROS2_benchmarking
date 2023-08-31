#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def shutdown_node():
    rospy.signal_shutdown("Shutdown Requested")

def talker():
    pub = rospy.Publisher('chat', String, queue_size=30000)
    rospy.init_node('speaker', anonymous=True)
    integers = [i for i in range(10,201,10)]
    frequencies = [i for i in range(10,201,10)]
    while not rospy.is_shutdown():
        for i in integers:
            msg = "a"*1024*i
            for j in frequencies:
                rate = rospy.Rate(j)
                for k in range(1000):
                    pub.publish(msg)
                    rospy.loginfo(f"{i},{j},{k}")
                    rate.sleep()
                rospy.sleep(10.)
            rospy.sleep(10.)
        shutdown_node()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
