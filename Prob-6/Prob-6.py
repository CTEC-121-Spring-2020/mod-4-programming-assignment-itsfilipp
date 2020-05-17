# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Filipp Kopytyuk

from graphics import *

def main():

    win = GraphWin("Lego", 1100, 1100)

    blueLegoBrick = Rectangle(Point(5, 100), Point(260,50))
    blueLegoBrick.setOutline("black")
    blueLegoBrick.setFill("blue")
    blueLegoBrick.setWidth(5)
    blueLegoBrick.draw(win)

    blueBricksnibs = Rectangle(Point(15, 50), Point(40, 40))
    blueBricksnibs.setFill("blue")
    blueBricksnibs.setOutline("black")
    blueBricksnibs.setWidth(5)
    blueBricksnibs.draw(win)

    for i in range(1,5):
        blueBricksNextnibs = blueBricksnibs.clone()
        blueBricksNextnibs.move(50 *i, 0)
        blueBricksNextnibs.draw(win)
    
    greenLegoBrick = blueLegoBrick.clone()
    greenLegoBrick.setFill("green")
    greenLegoBrick.setOutline("black")
    greenLegoBrick.setWidth(5)
    greenLegoBrick.move(350,0)
    greenLegoBrick.draw(win)

    greenBricknibs = blueBricksnibs.clone()
    greenBricknibs.setFill("green")
    greenBricknibs.setOutline("black")
    greenBricknibs.setWidth(5)
    greenBricknibs.move(350,0)
    greenBricknibs.draw(win)

    for i in range(5):
        greenBrickNextnibs = greenBricknibs.clone()
        greenBrickNextnibs.move(50 *i, 0)
        greenBrickNextnibs.draw(win)

    yellowLegoBrick = blueLegoBrick.clone()
    yellowLegoBrick.setFill("yellow")
    yellowLegoBrick.setOutline("black")
    yellowLegoBrick.setWidth(5)
    yellowLegoBrick.move(0, 100)
    yellowLegoBrick.draw(win)

    yellowBricknibs = blueBricksnibs.clone()
    yellowBricknibs.setFill("yellow")
    yellowBricknibs.setOutline("black")
    yellowBricknibs.setWidth(5)
    yellowBricknibs.move(0, 100)
    yellowBricknibs.draw(win)

    for i in range(5):
            yellowBrickNextnibs = yellowBricknibs.clone()
            yellowBrickNextnibs.move(50 *i, 0)
            yellowBrickNextnibs.draw(win)

    redLegoBrick = blueLegoBrick.clone()
    redLegoBrick.setFill("red")
    redLegoBrick.setOutline("black")
    redLegoBrick.setWidth(5)
    redLegoBrick.move(350, 100)
    redLegoBrick.draw(win)

    redBricknibs = blueBricksnibs.clone()
    redBricknibs.setFill("red")
    redBricknibs.setOutline("black")
    redBricknibs.setWidth(5)
    redBricknibs.move(350,100)
    redBricknibs.draw(win)

    for i in range(5):
        redBrickNextnibs = redBricknibs.clone()
        redBrickNextnibs.move(50 *i, 0)
        redBrickNextnibs.draw(win)

    cyanLegoBrick = blueLegoBrick.clone()
    cyanLegoBrick.setFill("cyan")
    cyanLegoBrick.setOutline("black")
    cyanLegoBrick.setWidth(5)
    cyanLegoBrick.move(0, 200)
    cyanLegoBrick.draw(win)

    cyanBricknibs = blueBricksnibs.clone()
    cyanBricknibs.setFill("cyan")
    cyanBricknibs.setOutline("black")
    cyanBricknibs.setWidth(5)
    cyanBricknibs.move(0,200)
    cyanBricknibs.draw(win)

    for i in range(5):
        cyanBrickNextnibs = cyanBricknibs.clone()
        cyanBrickNextnibs.move(50 *i, 0)
        cyanBrickNextnibs.draw(win)

    blackLegoBrick = blueLegoBrick.clone()
    blackLegoBrick.setFill("black")
    blackLegoBrick.setOutline("red")
    blackLegoBrick.setWidth(5)
    blackLegoBrick.move(350,200)
    blackLegoBrick.draw(win)

    blackBricknibs = blueBricksnibs.clone()
    blackBricknibs.setFill("black")
    blackBricknibs.setOutline("red")
    blackBricknibs.setWidth(5)
    blackBricknibs.move(350,200)
    blackBricknibs.draw(win)

    for i in range(5):
        blackBrickNextnib = blackBricknibs.clone()
        blackBrickNextnib.move(50*i, 0)
        blackBrickNextnib.draw(win)

    win.getMouse()
    win.close()



main()