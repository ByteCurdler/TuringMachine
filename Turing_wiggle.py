#!/usr/bin/python3

states = (
    (   #A (index 0)
        (1, 1,  1), #0, (BitToWrite, MoveBy, NextStateIndex)
        (1, 1,  1)  #1
    ), ( #B (index 1)
        (1, 0, 2),
        (1, -1, 1)
    ), ( #C (index 2)
        (1, 0, 1),
        (1, 1, 2)
    )
)
