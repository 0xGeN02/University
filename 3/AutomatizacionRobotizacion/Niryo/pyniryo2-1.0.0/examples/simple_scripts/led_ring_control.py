"""
Little Script which shows how to control Ned's Led Ring with PyNiryo2
"""
# !/usr/bin/env python

from pyniryo2 import NiryoRobot
import sys, time

if sys.version_info[0] == 2:
    input_func = raw_input
else:
    input_func = input

simulation = "-simu" in sys.argv
robot_ip_address_rpi = "10.10.10.10"
robot_ip_address_simu = "127.0.0.1"
robot_ip_address = robot_ip_address_simu if simulation else robot_ip_address_rpi

# Connecting to robot
niryo_robot = NiryoRobot(ip_address=robot_ip_address)

print('SOLID')
niryo_robot.led_ring.solid([255, 0, 0])

time.sleep(4)

print('FLASH 8 Hz 10 times and wait for the end')
niryo_robot.led_ring.flash([20, 255, 78], iterations=10, wait=True, frequency=8)

print('ALTERNATE 8 times')
niryo_robot.led_ring.alternate([[0, 255, 0], [255, 0, 0], [0, 0, 255]], iterations=8)

time.sleep(4)

print('CHASE with 100ms between each step ')
niryo_robot.led_ring.chase([178, 78, 100], speed=100)

time.sleep(4)

print('WIPE 3 times with 90ms between each step, wait for the end')
niryo_robot.led_ring.wipe([98, 78, 190], speed=90, wait=True)

print('RAINBOW 2 times with 10ms between each step ')
niryo_robot.led_ring.rainbow(speed=10, iterations=2)

time.sleep(4)

print('RAINBOW CYCLE endless')
niryo_robot.led_ring.rainbow_cycle()

time.sleep(4)

print('RAINBOW CHASE endless')
niryo_robot.led_ring.rainbow_chase()

time.sleep(4)

print('GO UP 4 times with 70ms between each step, wait for the end')
niryo_robot.led_ring.go_up([189, 96, 113], iterations=4, speed=70, wait=True)

print('GO UP AND DOWN 5 times, wait for the end')
niryo_robot.led_ring.go_up_down([70, 167, 97], iterations=5, wait=True)

time.sleep(4)

print('Turn off Leds')
niryo_robot.led_ring.turn_off()

# Close
niryo_robot.end()
