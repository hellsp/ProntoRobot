# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 18:45
# @Author  : 'ShawnTT'
# @FileName: classRobot.py
# @Project: ProntoRobot


class Robot:
    def __init__(self, position=[0, 0], direction='N'):
        self.__position = position
        self.__direction = direction  # 'N'orth, 'S'outh, 'E'ast, 'W'est

    def get_position(self):
        return self.__position

    def get_direction(self):
        return self.__direction

    def set_position(self, X=0, Y=0):
        self.__position = [X, Y]

    def set_direction(self,D):
        self.__direction = D

    def __str__(self):
        return "Robot's position is " + str(self.__position) \
                + ", direction is : " + str(self.__direction)
