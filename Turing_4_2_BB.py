#!/usr/bin/python3
# 4        2             BB
# |        |         ___/¯¯\__
# |        |        |         |
# 4 state, 2 symbol busy beaver
states = (
    (   #A (index 0)
        (1, 1,  1), #0, (BitToWrite, MoveBy, NextStateIndex)
        (1, -1, 1)  #1
    ), ( #B (index 1)
        (1, -1, 0),
        (0, -1, 2)
    ), ( #C (index 2)
        (1, 1, -1),
        (1, -1, 3)
    ), ( #D (index 3)
        (1, 1, 3),
        (0, 1, 0)
    )
)
