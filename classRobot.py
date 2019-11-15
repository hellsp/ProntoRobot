# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 18:45
# @Author  : 'ShawnTT'
# @FileName: classRobot.py
# @Project: ProntoRobot


class Robot:
    # A new Robot initialization
    # if not specified, initial Position is (0,0), initial Direct is North
    def __init__(self, p=[0, 0], d='N'):
        self.__position = p
        self.__direction = d  # 'N'orth, 'S'outh, 'E'ast, 'W'est

    def get_position(self):
        return self.__position

    def get_direction(self):
        return self.__direction

    def set_position(self, x=0, y=0):
        self.__position = [x, y]

    def set_direction(self, d):
        self.__direction = d

    def __str__(self):
        return "Robot's position is " + str(self.__position) \
                + ", direction is : " + str(self.__direction)
