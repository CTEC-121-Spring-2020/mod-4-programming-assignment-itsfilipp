# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Filipp Kopytyuk

from graphics import *

def main():
    win = GraphWin("House", 900, 900)
    win.setCoords(0,0, 100, 100)
    
    P1 = win.getMouse()
    P2 = win.getMouse()
    square = Rectangle(P1, P2)
    square.draw(win)
    framebottomY = min(P1.getY(), P2.getY())
    frametopY = max(P1.getY(), P2.getY())
    frameleftX = min(P1.getX(), P2.getX())
    framerightX = max(P1.getX(), P2.getX())

    P3 = win.getMouse()
    frontdoorwidth = abs(P1.getX() - P2.getX()) * 0.1
    frontdoorheight = abs(P3.getY() - framebottomY)
    frontdoorP1 = Point(P3.getX() - frontdoorwidth * 0.5, framebottomY)
    frontdoorP2 = Point(P3.getX() + frontdoorwidth * 0.5, P3.getY())
    frontdoor = Rectangle(frontdoorP1, frontdoorP2)
    frontdoor.draw(win)

    P4 = win.getMouse()
    windowheight = frontdoorwidth * 0.5
    windowP1 = Point(P4.getX() - windowheight * 0.5, P4.getY() - windowheight * 0.5)
    windowP2 = Point(P4.getX() + windowheight * 0.5, P4.getY() + windowheight * 0.5)
    window = Rectangle(windowP1, windowP2)
    window.draw(win)

    P5 = win.getMouse()
    roofP1 = Point(frameleftX, frametopY)
    roofP2 = Point(framerightX, frametopY)
    roofP3 = P5
    roof = Polygon(roofP1, roofP2, roofP3)
    roof.draw(win)
    win.getMouse()
    win.close()


main()