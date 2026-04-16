import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import Float64

class HumiditySensor(Node):
    def __init__(self):
        super().__init__('humidity_sensor')
        self.publisher = self.create_publisher(Float64, 'kuca/vlaznost', 10)
        self.timer = self.create_timer(1.0, self.on_timer)
        
    def on_timer(self):
        h_low = 30
        h_high = 70
        msg = Float64()
        msg.data = random.uniform(h_low, h_high)
        self.publisher.publish(msg)
        self.get_logger().info(f"Humidity sensor reading: {msg.data:.2f} %")
        
def main():
    rclpy.init()
    node = HumiditySensor()
    rclpy.spin(node)
