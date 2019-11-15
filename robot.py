# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 19:05
# @Author  : 'ShawnTT'
# @FileName: robot.py
# @Project: ProntoRobot

import ctrlRobot
C = ctrlRobot


def main():
    inputs = "F1,R1,B2,L1,B3"
    for s in inputs.strip().split(','):
        robotAction = s[:1]
        actionUnits = int(s[1:])
        #print(robotAction, actionUnits)
        if robotAction == 'F':
            C.robot_forward(actionUnits)
        elif robotAction == 'B':
            C.robot_backward(actionUnits)
        elif robotAction == 'R':
            while actionUnits:
                C.robot_turn_right()
                actionUnits -= 1
        elif robotAction == 'L':
            while actionUnits:
                C.robot_turn_left()
                actionUnits -= 1
    print("\n== Robot's position and direction ==\n",
          C.robot_where(), C.robot_face_to())


main()

