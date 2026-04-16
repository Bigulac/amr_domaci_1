import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, Int64

class Dashboard(Node):
    def __init__(self):
        super().__init__('dashboard')
        
        self.temperature = None
        self.humidity = None
        self.luminosity = None
        
        self.subscription = self.create_subscription(
            Float64,
            'kuca/temperatura',
            self.temperature_callback,
            10)
        self.subscription = self.create_subscription(
            Float64,
            'kuca/vlaznost',
            self.humidity_callback,
            10)
        self.subscription = self.create_subscription(
            Int64,
            'kuca/osvetljenje',
            self.luminosity_callback,
            10)
        self.subscription # prevent unused variable warning
        
        self.timer = self.create_timer(1.0, self.log_all)
        
    def temperature_callback(self, msg):
        self.temperature = msg.data

    def humidity_callback(self, msg):
        self.humidity = msg.data

    def luminosity_callback(self, msg):
        self.luminosity = msg.data

    def log_all(self):
        if None in (self.temperature, self.humidity, self.luminosity):
            self.get_logger().info("Waiting for all sensor data...")
            return

        self.get_logger().info(f"[Nadzorna tabla] Temperatura: {self.temperature:.2f} C | Vlaznost: {self.humidity:.2f} % | Osvetljenje: {self.luminosity} lux")
        
def main():
    rclpy.init()
    node = Dashboard()
    rclpy.spin(node)
