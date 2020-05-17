# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Filipp Kopytyuk

from graphics import *

def main():
    win = GraphWin("Face", 1000,1000)
    center = Point(500, 500)

    leftEar = Circle(center, 50)
    leftEar.move(300,0)
    leftEar.setFill("yellow")
    leftEar.setOutline("black")
    leftEar.draw(win)

    rightEar = Circle(center, 50)
    rightEar.move(-300, 0)
    rightEar.setFill("yellow")
    rightEar.setOutline("black")
    rightEar.draw(win)

    faceStructure = Circle(center, 300)
    faceStructure.setFill("yellow")
    faceStructure.setOutline("black")
    faceStructure.draw(win)

    leftEye = Circle(center, 40)
    leftEye.setFill("white")
    leftEye.setOutline("white")
    leftEye.move(-100,-50)
    leftEye.draw(win)

    leftEye = Circle(center, 20)
    leftEye.setFill("black")
    leftEye.setOutline("black")
    leftEye.move(-100,-50)
    leftEye.draw(win)

    rightEye = Circle(center, 40)
    rightEye.setFill("white")
    rightEye.setOutline("white")
    rightEye.move(100,-50)
    rightEye.draw(win)

    rightEye = Circle(center, 20)
    rightEye.setFill("black")
    rightEye.setOutline("black")
    rightEye.move(100,-50)
    rightEye.draw(win)

    nose = Polygon(Point(500,500), Point(450,550), Point(550,550))
    nose.setFill("black")
    nose.setOutline("black")
    nose.draw(win)

    ovalMouth = Oval(Point(650, 750), Point(350,600))
    ovalMouth.setFill("black")
    ovalMouth.setOutline("red")
    ovalMouth.draw(win)

    tooth = Rectangle(Point(475, 650), Point(500, 600))
    tooth.setFill("white")
    tooth.setOutline("black")
    tooth.draw(win)


    hairone = Line(Point(200, 100), Point(500, 200))
    hairone.setFill("white")
    hairone.setOutline("black")
    hairone.draw(win)

    hairtwo = Line(Point(250, 150), Point(650,250))
    hairtwo.setFill("white")
    hairtwo.setOutline("black")
    hairtwo.draw(win)

    win.getMouse()
    win.close()



main()