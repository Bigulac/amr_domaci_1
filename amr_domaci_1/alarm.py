import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool
from std_msgs.msg import Float64


class Alarm(Node):
    def __init__(self):
        super().__init__('alarm')

        self.alarm_active = False

        self.srv = self.create_service(
            SetBool,
            'kuca/alarm/aktiviraj',
            self.handle_alarm
        )

        self.create_subscription(
            Float64,
            'kuca/temperatura',
            self.temp_callback,
            10
        )

    def handle_alarm(self, request, response):
        self.alarm_active = request.data

        if self.alarm_active:
            response.message = "Alarm aktiviran."
        else:
            response.message = "Alarm deaktiviran."

        response.success = True

        self.get_logger().info(response.message)
        return response

    def temp_callback(self, msg):
        if not self.alarm_active:
            return

        temp = msg.data

        if temp < 15 or temp > 35:
            self.get_logger().warn(
                f"ALARM! Temperatura van opsega: {temp:.2f} C"
            )


def main():
    rclpy.init()
    node = Alarm()
    rclpy.spin(node)