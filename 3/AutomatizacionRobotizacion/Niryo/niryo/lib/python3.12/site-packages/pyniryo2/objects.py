#!/usr/bin/env python
# coding=utf-8

from time import time
import numpy as np


class PoseObject:
    """
    Pose object which stores x, y, z, roll, pitch & yaw parameters

    :ivar x: X (meter)
    :vartype x: float
    :ivar y: Y (meter)
    :vartype y: float
    :ivar z: Z (meter)
    :vartype z: float
    :ivar roll: Roll (radian)
    :vartype roll: float
    :ivar pitch: Pitch (radian)
    :vartype pitch: float
    :ivar yaw: Yaw (radian)
    :vartype yaw: float

    """

    def __init__(self, x, y, z, roll, pitch, yaw):
        # X (meter)
        self.x = float(x)
        # Y (meter)
        self.y = float(y)
        # Z (meter)
        self.z = float(z)
        # Roll (radian)
        self.roll = float(roll)
        # Pitch (radian)
        self.pitch = float(pitch)
        # Yaw (radian)
        self.yaw = float(yaw)

    def __str__(self):
        position = "x = {:.4f}, y = {:.4f}, z = {:.4f}".format(self.x, self.y, self.z)
        orientation = "roll = {:.3f}, pitch = {:.3f}, yaw = {:.3f}".format(self.roll, self.pitch, self.yaw)
        return position + "\n" + orientation

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        roll = self.roll + other.roll
        pitch = self.pitch + other.pitch
        yaw = self.yaw + other.yaw
        return PoseObject(x, y, z, roll, pitch, yaw)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        roll = self.roll - other.roll
        pitch = self.pitch - other.pitch
        yaw = self.yaw - other.yaw
        return PoseObject(x, y, z, roll, pitch, yaw)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z \
               and self.roll == other.roll and self.pitch == other.pitch and self.yaw == other.yaw

    def copy_with_offsets(self, x_offset=0., y_offset=0., z_offset=0., roll_offset=0., pitch_offset=0., yaw_offset=0.):
        """
        Create a new pose from copying from copying actual pose with offsets

        :rtype: PoseObject
        """
        return PoseObject(self.x + x_offset,
                          self.y + y_offset,
                          self.z + z_offset,
                          self.roll + roll_offset,
                          self.pitch + pitch_offset,
                          self.yaw + yaw_offset)

    def to_list(self):
        """
        Return a list [x, y, z, roll, pitch, yaw] corresponding to the pose's parameters

        :rtype: list[float]
        """
        list_pos = [self.x, self.y, self.z, self.roll, self.pitch, self.yaw]
        return list(map(float, list_pos))

    @property
    def quaternion(self):
        """
        Return the quaternion in a list [qx, qy, qz, qw]

        :return: quaternion [qx, qy, qz, qw]
        :rtype: list[float, float, float, float]
        """
        return self.euler_to_quaternion(self.roll, self.pitch, self.yaw)

    @property
    def quaternion_pose(self):
        """
        Return the position and the quaternion in a list [x, y, z, qx, qy, qz, qw]

        :return: position [x, y, z] + quaternion [qx, qy, qz, qw]
        :rtype: list[float, float, float, float, float, float, float]

        """
        return [self.x, self.y, self.z] + list(self.euler_to_quaternion(self.roll, self.pitch, self.yaw))

    @staticmethod
    def euler_to_quaternion(roll, pitch, yaw):
        """
        Convert euler angles to quaternion

        :param roll: roll in radians
        :type roll: float
        :param pitch: pitch in radians
        :type pitch: float
        :param yaw: yaw in radians
        :type yaw: float
        :return: quaternion in a list [qx, qy, qz, qw]
        :rtype: list[float, float, float, float]
        """
        qx = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(
            yaw / 2)
        qy = np.cos(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.cos(pitch / 2) * np.sin(
            yaw / 2)
        qz = np.cos(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2) - np.sin(roll / 2) * np.sin(pitch / 2) * np.cos(
            yaw / 2)
        qw = np.cos(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.sin(pitch / 2) * np.sin(
            yaw / 2)

        return [qx, qy, qz, qw]

    @staticmethod
    def quaternion_to_euler_angle(qx, qy, qz, qw):
        """
        Convert euler angles to quaternion

        :param qx:
        :type qx: float
        :param qy:
        :type qy: float
        :param qz:
        :type qz: float
        :param qw:
        :type qw: float
        :return: euler angles in a list [roll, pitch, yaw]
        :rtype: list[float, float, float]
        """
        ysqr = qy * qy

        t0 = +2.0 * (qw * qx + qy * qz)
        t1 = +1.0 - 2.0 * (qx * qx + ysqr)
        roll = np.arctan2(t0, t1)

        t2 = +2.0 * (qw * qy - qz * qx)

        t2 = np.clip(t2, a_min=-1.0, a_max=1.0)
        pitch = np.arcsin(t2)

        t3 = +2.0 * (qw * qz + qx * qy)
        t4 = +1.0 - 2.0 * (ysqr + qz * qz)
        yaw = np.arctan2(t3, t4)

        return roll, pitch, yaw


class TrajectoryObject():

    def __init__(self, name, description, joint_names, points, accelerations, velocities, time_from_start):
        self.name = name
        self.description = description
        self.joint_names = joint_names
        self.points = points
        self.accelerations = accelerations
        self.velocities = velocities
        self.time_from_start = time_from_start
