import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class SpeakerNode(Node):
    def __init__(self):
        super().__init__('throughput')
        self.publisher_ = self.create_publisher(String, 'chat', 30000)
        self.msg_sizes = [j for j in range(10,141,10)]
        self.frequency = 10 # increment from 10 to 200
        timer_period = 1/self.frequency
        for i in self.msg_sizes:
            msg_data = "a"*1024*i
            msg = String()
            msg.data = msg_data
            start_time = time.time()
            while time.time() - start_time <30:
                self.timer_= self.create_timer(timer_period, self.run(msg,i,self.frequency))
            time.sleep(15)

    def run(self,message,size,frequency):
        self.publisher_.publish(message)
        self.get_logger().info(f"{size},{frequency}")              

def main(args=None):
    rclpy.init(args=args)
    speaker_node = SpeakerNode()
    try:
        speaker_node.run()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()