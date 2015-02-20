#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program will evaluate blood pressure reading and output a message."""

BP_READING = int(raw_input('What is your blood pressure? '))

if BP_READING <= 89:
    BP_STATUS = 'Low'
elif 90 <= BP_READING <= 119:
    BP_STATUS = 'Ideal'
elif 120 <= BP_READING <= 139:
    BP_STATUS = 'Warning'
elif 140 <= BP_READING <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

BP_MSG = 'Your status is currently: {}!'.format(BP_STATUS)
print BP_MSG
