#!/usr/bin/env python
# coding=utf-8

from pyniryo2.led_ring.enums import AnimationMode, LedMode


class LedRingStatusObject:
    """
    Object used to store Led Ring status
    """

    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

        self.animation = AnimationMode.UNKNOWN
        self.mode = LedMode.UNKNOWN

    def init_from_message(self, msg):
        self.r = msg['animation_color']['r']
        self.g = msg['animation_color']['g']
        self.b = msg['animation_color']['b']

        self.animation = AnimationMode(msg['animation_mode']['animation'])
        self.mode = LedMode(msg['led_mode'])
