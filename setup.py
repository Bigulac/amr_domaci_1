from setuptools import find_packages, setup

package_name = 'amr_domaci_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cevilko',
    maintainer_email='cevilko@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'temperature_sensor = amr_domaci_1.temperature_sensor:main',
            'humidity_sensor = amr_domaci_1.humidity_sensor:main',
            'luminosity_sensor = amr_domaci_1.luminosity_sensor:main',
            'dashboard = amr_domaci_1.dashboard:main'
        ],
    },
)
