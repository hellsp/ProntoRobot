# -*- coding: utf-8 -*-
# @Time    : 14/11/2019 19:05
# @Author  : 'ShawnTT'
# @FileName: robot.py
# @Project: ProntoRobot

import ctrlRobot
C = ctrlRobot


def main():
    print("\n======= Pronto Cloud Robot =======\n")

    # for test, please input "F1,R1,B2,L1,B3"
    robotMove = {}
    Verified = False
    while not Verified:
        inputs = input("Please input commands to move the Robot: ").upper().strip().replace(' ', '').split(',')

        # remove empty items from the inputs
        inputs = [x for x in inputs if x]

        # determine commands in the inputs
        for s in inputs:
            act = s[:1]
            units = s[1:]

            # determine invalid input commands
            if act not in ('F', 'B', 'R', 'L') or not units.isdigit():
                print("Invalid input!", act, " - ", units)
                Verified = False
            else:
                robotMove[act] = int(units)
                Verified = True

    # process inputted commands to move the Robot
    startPos = C.robot_where()
    for a in robotMove:
        u = robotMove[a]

        # move the Robot based on the commands
        if a == 'F':
            C.robot_forward(u)
        elif a == 'B':
            C.robot_backward(u)
        elif a == 'R':
            while u:
                C.robot_turn_right()
                u -= 1
        elif a == 'L':
            while u:
                C.robot_turn_left()
                u -= 1

    # output the minimum distance to initial point
    stopPos = C.robot_where()
    d = C.get_distance(startPos, stopPos)
    # print(stopPos)
    print("\nThe minimum distance backs to start point is: ", d)
    print("\n")


main()

