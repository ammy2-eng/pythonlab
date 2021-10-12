#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:36:28 2021

@author: bdtech
"""

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split()
    for key in keys:
        value = 1
        print("%s\t%d" % (key,value))