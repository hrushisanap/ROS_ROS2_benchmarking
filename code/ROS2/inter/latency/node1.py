
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class SpeakerNode(Node):
    def __init__(self):
        super().__init__('speaker')
        self.publisher_ = self.create_publisher(String, 'chat', 30000)
        self.frequency = 10 # increment from 10 to 200
        timer_period = 1/self.frequency
        self.timer_= self.create_timer(timer_period, self.run())

    def run(self):
        msg_size = [i for i in range(10,201,10)]
        for i in msg_size:
            msg_data = "a"*1024*i
            msg = String()
            msg.data = msg_data
            for k in range(1500):
                self.publisher_.publish(msg)
                self.get_logger().info(f"{i},{self.frequency},{k}")
            time.sleep(15)

def main(args=None):
    rclpy.init(args=args)
    speaker_node = SpeakerNode()
    try:
        rclpy.spin(speaker_node)
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()


