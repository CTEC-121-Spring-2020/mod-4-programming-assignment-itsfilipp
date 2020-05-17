# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Filipp Kopytyuk

from graphics import *

def main():
     # opens window with title "Shape" and size of (400, 400)
     win = GraphWin("Shape", 400, 400)
     # drawing your shape onto window
     P1 = Point(50, 50)
     P2 = Point(100, 100)
     shape = Rectangle(P1, P2)
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     # draws shape defines below 5 times wherever you click the mouse on the window
     for i in range(5):
          p = win.getMouse()
          shape = Rectangle(p, Point(p.getX() + 50, p.getY() + 50))
          shape.setOutline("red")
          shape.setFill("red")
          shape.draw(win)
     # writes a string in the middle of window after the last possible click and closes window
     Text(Point(200, 200), "Click again to quit").draw(win)
     win.getMouse()
     win.close()

main()