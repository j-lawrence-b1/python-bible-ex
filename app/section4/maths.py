#!/usr/bin/env python3

import math


def round(x):
    if x < 5:
        return math.floor(x)
    else:
        return math.ceil(x)
