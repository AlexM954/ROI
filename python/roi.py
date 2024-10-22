# Implementation of the ROI algorithm in Python.

from copy import deepcopy

import numpy as np


t = {
    "x": None,
    "y": None,
    "mean": 0,
    "done": False,
    "extended": False
}


def new(x, y):
    roi = deepcopy(t)
    roi["x"] = np.asarray([x])
    roi["y"] = np.asarray([y])
    roi["mean"] = y

    return roi


def mean(roi):
    roi["mean"] = np.mean(roi["y"])


def extend(roi, x, y):
    roi["x"] = np.append(roi["x"], x)
    roi["y"] = np.append(roi["y"], y)
    mean(roi)
