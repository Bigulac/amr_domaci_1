import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import Float64

class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher = self.create_publisher(Float64, 'kuca/temperatura', 10)
        self.timer = self.create_timer(1.0, self.on_timer)
        
    def on_timer(self):
        t_low = 18
        t_high = 30
        msg = Float64()
        msg.data = random.uniform(t_low, t_high)
        self.publisher.publish(msg)
        self.get_logger().info(f"Temperature sensor reading: {msg.data:.2f} C")
        
def main():
    rclpy.init()
    node = TemperatureSensor()
    rclpy.spin(node)
