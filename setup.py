import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'bcap_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.rviz'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Isao Hara',
    maintainer_email='hara@rt-net.jp',
    description='Cobotta controller by b-cap',
    license='Apache License v2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bcap_controller = bcap_controller.joint_control:main',
        ],
    },
)
