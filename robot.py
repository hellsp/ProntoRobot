# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 19:05
# @Author  : 'ShawnTT'
# @FileName: robot.py
# @Project: ProntoRobot

import ctrlRobot
ctrl = ctrlRobot


def main():
    # inputs = "F1,R1,B2,L1,B3"
    # steps = {}
    # for s in inputs.split(','):
    #     steps[s[:1]] = s[1:]
    # print(steps)
    # print(robot_forward())

    print(ctrl.robot_where())
    print(ctrl.robot_face_to())

    ctrl.robot_forward(3)
    ctrl.robot_turn_right()
    ctrl.robot_backward(5)

    print(ctrl.robot_where())
    print(ctrl.robot_face_to())


    ctrl.robot_turn_left()
    ctrl.robot_backward(5)
    ctrl.robot_forward(3)

    print(ctrl.robot_where())
    print(ctrl.robot_face_to())



    #
    # ctrl.robot_forward(3)
    # print(robot.get_direction())
    # print(robot.get_position())
    #
    # ctrl.robot_forward(-10)
    # print(robot.get_direction())
    # print(robot.get_position())

#    print(robot)
    #
    # robot_forward(1)
    # print(robot.get_direction())
    # print(robot.get_position())

    # for s in inputs.split(','):
    #     if s[:1] == 'F':
    #         unitsForward = s[1:]
    #         steps[]
    #
    #     elif s[:1] == 'B':
    #         unitsBackward = s[1:]
    #
    #     elif s[:1] == 'L':
    #         leftTurn = s[1:]
    #
    #     elif s[:1] == 'R':
    #         rightTurn = s[1:]
    #


            # print(s[1:])
            # print(s[1:2])
            #stepsForward = s[1:2]

        #print(s)
    #stepsForward = inputs.split(',')[0][1:2]


    #print(stepsForward)

    #robot = classRobot.Robot()




main()

