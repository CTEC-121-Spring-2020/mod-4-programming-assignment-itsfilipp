# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Filipp Kopytyuk

from graphics import *

def main():
    win = GraphWin("Archery target", 400, 400)
    Center = Point(200, 200)
    aCircle = Circle(Center, 150)
    aCircle.setFill("white")
    aCircle.draw(win)
    bCircle = Circle(Center, 120)
    bCircle.setFill("black")
    bCircle.draw(win)
    cCircle = Circle(Center, 90)
    cCircle.setFill("blue")
    cCircle.draw(win)
    dCircle = Circle(Center, 60)
    dCircle.setFill("red")
    dCircle.draw(win)
    eCircle = Circle(Center, 30)
    eCircle.setFill("yellow")
    eCircle.draw(win)
    win.getMouse()
    win.close()


main()    