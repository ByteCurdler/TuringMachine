import time, sys

VIEW_DISTANCE = 10

class TuringStrip():
    def __init__(self):
        self.data = []

    def __setitem__(self, n, value):
        if(value and (n not in self.data)):
            self.data.append(n)
        elif((not value) and (n in self.data)):
            del self.data[self.data.find(n)]

    def __getitem__(self, n):
        return (n in self.data)

def disp(phase):
    turingString = ""
    for i in range(head-VIEW_DISTANCE, head+VIEW_DISTANCE+1):
        if(i == 0):
            bw = "□■"
        else:
            bw = "◯●"
        turingString += bw[int(t[i])]
    sys.stdout.buffer.write(b"\033[34m" + turingString.encode("utf-8") + b"\n")
    print((" " * VIEW_DISTANCE) + "^" + (chr(65 + state) if state != -1 else "HALT"))
    print(phase + "                     \n\033[A\033[A\033[A\033[A")
    time.sleep(speed)
    
def turingDo(write, move, nextstate):
    global t, head, state
    if(write != -1):
        t[head] = write
    disp("WRITE " + str(write))
    head += move
    disp("MOVE BY " + str(move))
    state = nextstate
    disp("TO STATE " + (chr(65 + state) if state != -1 else "HALT"))

state = 0

t = TuringStrip()

head = 0

speed = float(input("\033[32mDelay?      " + ("\033[D" * 5)))

disp("STARTING POSITION")

from ThreeStateTwoSymbolBusyBeaver import states

while state != -1:
    read = t[head]
    turingDo(*states[state][read])
##    if(state == "A"):
##        if(read):
##            turingDo(1, -1, "C")
##        else:
##            turingDo(1, 1, "B")
##    elif(state == "B"):
##        if(read):
##            turingDo(1, 1, "B")
##        else:
##            turingDo(1, -1, "A")
##    elif(state == "C"):
##        if(read):
##            turingDo(1, 1, "HALT")
##        else:
##            turingDo(1, -1, "B")
print("\n\n")
