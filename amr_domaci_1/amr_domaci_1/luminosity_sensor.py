import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import Int64

class LuminositySensor(Node):
    def __init__(self):
        super().__init__('luminosity_sensor')
        self.publisher = self.create_publisher(Int64, 'kuca/osvetljenje', 10)
        self.timer = self.create_timer(1.0, self.on_timer)
        
    def on_timer(self):
        L_low = 0
        L_high = 1000
        msg = Int64()
        msg.data = round(random.uniform(L_low, L_high))
        self.publisher.publish(msg)
        self.get_logger().info(f"Luminosity sensor reading: {msg.data} lux")
        
def main():
    rclpy.init()
    node = LuminositySensor()
    rclpy.spin(node)
