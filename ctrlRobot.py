# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 23:31
# @Author  : 'ShawnTT'
# @FileName: ctrlRobot.py
# @Project: ProntoRobot

import classRobot
robot = classRobot.Robot()


def robot_forward(units):
    x, y = robot.get_position()
    d = robot.get_direction()
    if d == 'E':
        x += units
    elif d == 'N':
        y += units
    elif d == 'W':
        x -= units
    elif d == 'S':
        y -= units
    robot.set_position(x, y)
    return robot.get_position()


def robot_backward(units):
    x, y = robot.get_position()
    d = robot.get_direction()
    if d == 'E':
        x -= units
    elif d == 'N':
        y -= units
    elif d == 'W':
        x += units
    elif d == 'S':
        y += units
    robot.set_position(x, y)
    return robot.get_position()


def robot_turnleft():
    d = robot.get_direction()
    d_all = ['E', 'S', 'W', 'N']
