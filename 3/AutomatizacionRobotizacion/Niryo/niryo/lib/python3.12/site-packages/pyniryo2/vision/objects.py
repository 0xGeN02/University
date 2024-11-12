#!/usr/bin/env python
# coding=utf-8

from collections import namedtuple

CameraInfo = namedtuple("CameraInfo", ['intrinsics', 'distortion'])

ImageParameters = namedtuple("ImageParameters", ['brightness_factor', 'contrast_factor', 'saturation_factor'])
