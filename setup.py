from setuptools import setup, find_packages

setup(
    name='jetracer',
    version='0.0.0',
    description='An easy to use AI racecar powered by NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
	'Adafruit-PlatformDetect==3.13.0',
	'Adafruit-Blinka==6.10.3',
	'adafruit-circuitpython-busdevice==5.0.6',
	'adafruit-circuitpython-motor==3.3.0',
        'adafruit-circuitpython-servokit==1.2.2'
    ],
)
