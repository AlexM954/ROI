# Implementation of the ROI algorithm in Python.
# Standard library imports.
from copy import deepcopy

# External library imports.
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
    roi["extended"] = True

    return roi


def mean(roi):
    roi["mean"] = np.mean(roi["y"])


def extend(roi, x, y):
    roi["x"] = np.append(roi["x"], x)
    roi["y"] = np.append(roi["y"], y)
    mean(roi)


def closest_rel(roi, y, ppm):
    diff = abs((y / roi["mean"] - 1) * 1E6)
    closest = np.min(diff)

    if closest < ppm:
        return y[np.where(diff == closest)][0]

    else:
        return None


def closest_abs(roi, y, val):
    diff = abs(y - roi["mean"])
    closest = np.min(diff)

    if closest < val:
        return y[np.where(diff == closest)][0]

    else:
        return None


def cleanup(roi, minlen):
    if roi["done"] is True or roi["extended"] is True:
        return roi
    elif roi["extended"] is False and roi["done"] is False:
        if roi["x"].size > minlen:
            roi["done"] = True
            return roi


def detect(x, y, val, minlen, compare=closest_abs):
    roi_list = [new(x[0], i) for i in y[0]]

    for x, y in zip(x[1:], y[1:]):
        used_y = np.empty(0)
        # Attempt to extend each roi.
        for roi in roi_list:
            if roi["done"] is False:
                closest = compare(roi, y, val)
                if not closest:
                    roi["extended"] = False
                else:
                    used_y = np.append(used_y, closest)
                    extend(roi, x, closest)
        # Clean up the roilist by removing non-extended short roi.
        roi_list = [cleanup(roi, minlen) for roi in roi_list]

        # Extend the roilist with roi from y values that were not used.
        unused = np.setdiff1d(y, used_y)
        roi_list.extend(new(x, y) for y in unused)

    return roi_list
