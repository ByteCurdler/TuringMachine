import time, sys, pygcurse, pygame

VIEW_DISTANCE = 15
FONTSIZE = 10
STATECOLORS = ["red", (0, 255, 255), (0, 255, 0)]

class TuringStrip():
    def __init__(self):
        self.data = []

    def __setitem__(self, nn, value):
        n = tuple(nn)
        if(value and (n not in self.data)):
            self.data.append(n)
        elif((not value) and (n in self.data)):
            del self.data[self.data.index(n)]

    def __getitem__(self, nn):
        n = tuple(nn)
        return (n in self.data)

def disp():
    turingString = ""
    for i in range(head[0]-VIEW_DISTANCE, head[0]+VIEW_DISTANCE+1):
        for j in range(head[1]-VIEW_DISTANCE, head[1]+VIEW_DISTANCE+1):
            if(i == 0 and j == 0):
                bw = "◇◆"
            elif(i == 0 or j == 0):
                bw = "□■"
            else:
                bw = "◯●"
            bw = bw[0] + "█"
            turingString += bw[int(t[i, j])]
        turingString += "\n"
    win.putchars(turingString, fgcolor=(0, 255, 0), bgcolor="black")
    i, j = head
    if(i == 0 and j == 0):
        bw = "◇◆"
    elif(i == 0 or j == 0):
        bw = "□■"
    else:
        bw = "◯●"
    win.putchar(bw[int(t[i, j])], x=VIEW_DISTANCE, y=VIEW_DISTANCE, fgcolor=STATECOLORS[state])
    win.update()
    time.sleep(speed)

def turingDo(write, turn, nextstate):
    global t, head, dir, state
    if(write != -1):
        t[head] = write
    dir = (dir + turn) % 4
    state = nextstate

head = [0, 0]
dir = 3

t = TuringStrip()
pygame.init()
win = pygcurse.PygcurseWindow((VIEW_DISTANCE * 2) + 1,
                              (VIEW_DISTANCE * 2) + 1,
                              "Turmites",
                              font=pygame.font.SysFont("wenquanyimicroheimono", FONTSIZE))

speed = 0.01
state = 0
moves = 0
disp()

from Worm_Lantingtons_Ant import states

import random
while True:
    read = t[head]
    turingDo(*states[state][read])
    if(dir == 0):
        head[1] += 1
    elif(dir == 1):
        head[0] += 1
    elif(dir == 2):
        head[1] -= 1
    elif(dir == 3):
        head[0] -= 1
    moves += 1
    disp()
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

