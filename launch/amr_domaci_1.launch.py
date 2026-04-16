from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='amr_domaci_1',
            executable='temperature_sensor',
            name='temperature_sensor',
            output='screen',
        ),
        Node(
            package='amr_domaci_1',
            executable='humidity_sensor',
            name='humidity_sensor',
            output='screen',
        ),
        Node(
            package='amr_domaci_1',
            executable='luminosity_sensor',
            name='luminosity_sensor',
            output='screen',
        ),
        Node(
            package='amr_domaci_1',
            executable='dashboard',
            name='dashboard',
            output='screen',
        ),
        Node(
            package='amr_domaci_1',
            executable='lock',
            name='lock',
            output='screen',
        ),
        Node(
            package='amr_domaci_1',
            executable='alarm',
            name='alarm',
            output='screen',
        ),
    ])