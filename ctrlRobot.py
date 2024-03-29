# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 23:31
# @Author  : 'ShawnTT'
# @FileName: ctrlRobot.py
# @Project: ProntoRobot

import classRobot
R = classRobot.Robot()  # can specify Robot's initial point:e.g. (p=[1,1], d='S')


def robot_where():
    return R.get_position()


def robot_face_to():
    return R.get_direction()


def robot_forward(units):
    x, y = R.get_position()
    d = R.get_direction()
    if d == 'E':
        x += units
    elif d == 'N':
        y += units
    elif d == 'W':
        x -= units
    elif d == 'S':
        y -= units
    return R.set_position(x, y)


def robot_backward(units):
    x, y = R.get_position()
    d = R.get_direction()
    if d == 'E':
        x -= units
    elif d == 'N':
        y -= units
    elif d == 'W':
        x += units
    elif d == 'S':
        y += units
    return R.set_position(x, y)


def robot_turn_left():
    d = R.get_direction()
    if d == 'E':
        d = 'N'
    elif d == 'N':
        d = 'W'
    elif d == 'W':
        d = 'S'
    elif d == 'S':
        d = 'E'
    return R.set_direction(d)


def robot_turn_right():
    d = R.get_direction()
    if d == 'E':
        d = 'S'
    elif d == 'S':
        d = 'W'
    elif d == 'W':
        d = 'N'
    elif d == 'N':
        d = 'E'
    return R.set_direction(d)


def get_distance(a, b):
    distance = abs(b[1] - a[1]) + abs(b[0] - a[0])
    return distance
