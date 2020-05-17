# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Filipp Kopytyuk

from graphics import *

def main():
   
    win = GraphWin("Car", 600, 600)
    # Car rear bumper
    P1 = Point(410, 375)
    P2 = Point(300, 310)
    rearBumper = Rectangle(P1, P2)
    rearBumper.setOutline("gray")
    rearBumper.setFill("gray")
    rearBumper.draw(win)
    # Car front bumper
    P1 = Point(90, 375)
    P2 = Point(110, 310)
    frontBumper = Rectangle(P1, P2)
    frontBumper.setOutline("gray")
    frontBumper.setFill("gray")
    frontBumper.draw(win)

    P1 = Point(400,375)
    P2 = Point(100, 300)
    # Car Frame
    carFrame = Rectangle(P1,P2)
    carFrame.setOutline("blue")
    carFrame.setFill("blue")
    carFrame.draw(win)
    # Rear wheel
    rearWheel = Circle(Point(350, 380), 30)
    rearWheel.setOutline("black")
    rearWheel.setFill("black")
    rearWheel.draw(win)
    # Front wheel
    frontWheel = Circle(Point(150, 380), 30)
    frontWheel.setOutline("black")
    frontWheel.setFill("black")
    frontWheel.draw(win)
    # Car Spoiler
    carPolygon = Polygon(Point(400,300), Point(400, 275), Point(390, 300))
    carPolygon.setOutline("gray")
    carPolygon.setFill("grey")
    carPolygon.draw(win)
    # Roof and windows
    aLine = Line(Point(150,300), Point(225, 265))
    aLine.setOutline("blue")
    aLine.setFill("blue")
    aLine.draw(win)
    
    bLine = Line(Point(225, 265), Point(300, 265))
    bLine.setOutline("blue")
    bLine.setFill("blue")
    bLine.draw(win)

    cLine = Line(Point(300,265), Point(350, 300))
    cLine.setOutline("blue")
    cLine.setFill("blue")
    cLine.draw(win)

    win.getMouse()
    win.close()
    
main()