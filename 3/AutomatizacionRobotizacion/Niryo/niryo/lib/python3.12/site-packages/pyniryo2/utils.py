"""
PyNiryo2 utils
-----------------
A collection of utilities to convert data from dict to list and vice versa
"""


def pose_dict_to_list(pose_dict):
    return [pose_dict["position"][axis] for axis in ["x", "y", "z"]] + \
           [pose_dict["rpy"][axis] for axis in ["roll", "pitch", "yaw"]]


def pose_list_to_dict(pose_list):
    return {"position": dict(zip(["x", "y", "z"], pose_list[:3])),
            "rpy": dict(zip(["roll", "pitch", "yaw"], pose_list[3:]))}


def pose_quat_dict_to_list(pose_dict):
    return [pose_dict["position"][axis] for axis in ["x", "y", "z"]] + \
           [pose_dict["orientation"][axis] for axis in ["x", "y", "z", "w"]]


def pose_quat_list_to_dict(pose_list):
    return {"position": dict(zip(["x", "y", "z"], pose_list[:3])),
            "orientation": dict(zip(["x", "y", "z", "w"], pose_list[3:]))}


def point_dict_to_list(pose_dict):
    return [pose_dict[axis] for axis in ["x", "y", "z"]]


def point_list_to_dict(pose_list):
    return dict(zip(["x", "y", "z"], pose_list[:3]))
