# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 23:31
# @Author  : 'ShawnTT'
# @FileName: ctrlRobot.py
# @Project: ProntoRobot

import classRobot
robot = classRobot.Robot()


def robot_where():
    return robot.get_position()


def robot_face_to():
    return robot.get_direction()


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


def robot_turn_left():
    d = robot.get_direction()
    if d == 'E':
        d = 'N'
    elif d == 'N':
        d = 'W'
    elif d == 'W':
        d = 'S'
    elif d == 'S':
        d = 'E'
    robot.set_direction(d)
    return robot.get_direction()


def robot_turn_right():
    d = robot.get_direction()
    if d == 'E':
        d = 'S'
    elif d == 'S':
        d = 'W'
    elif d == 'W':
        d = 'N'
    elif d == 'N':
        d = 'E'
    robot.set_direction(d)
    return robot.get_direction()