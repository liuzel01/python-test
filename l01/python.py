import tkinter
from socket import TIPC_SUBSCR_TIMEOUT
from typing import no_type_check_decorator

# NameError: name turtlr is not defined
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        tkinter.circle(rad, angle)
        tkinter.circle(-rad, angle)
    tkinter.circle(rad, angle/2)
    tkinter.fd(rad)
    tkinter.circle(neckrad+1, 180)
    tkinter.fd(rad*2/3)

def main():
    tkinter.setup(1300, 800, 0, 0)
    pythonsize = 30
    tkinter.pensize(pythonsize)
    tkinter.pencolor("blue")
    tkinter.seth(-40)
    drawSnake(40, 80, 5, pythonsize/2)

main()
