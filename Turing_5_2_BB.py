#!/usr/bin/python3
# 5        2             BB
# |        |         ___/¯¯\__
# |        |        |         |
# 5 state, 2 symbol busy beaver
states = (
    (   #A (index 0)
        (1, 1,  1), #0, (BitToWrite, MoveBy, NextStateIndex)
        (1, -1, 2)  #1
    ), ( #B (index 1)
        (1, 1, 2),
        (1, 1, 1)
    ), ( #C (index 2)
        (1, 1, 3),
        (0, -1, 4)
    ), ( #D (index 3)
        (1, -1, 0),
        (1, -1, 3)
    ), ( #E (index 4)
        (1, 1, -1),
        (0, -1, 0)
    )
)
