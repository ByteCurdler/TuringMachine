#!/usr/bin/python3
# 3        2             BB
# |        |         ___/¯¯\__
# |        |        |         |
# 3 state, 2 symbol busy beaver
states = (
    (   #A (index 0)
        (1, 1,  1), #0, (BitToWrite, MoveBy, NextStateIndex)
        (1, -1, 2)  #1
    ), ( #B (index 1)
        (1, -1, 0),
        (1, 1, 1)
    ), ( #C (index 2)
        (1, -1, 1),
        (1, 0, -1)
    )
)
