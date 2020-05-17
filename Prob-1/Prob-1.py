# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Filipp Kopytyuk

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


from graphics import *

def main():
     # creates the window
     win = GraphWin()
     # creates the shape you choose, plus adds the center point (for circle) with the designated radius
     shape = Circle(Point(50,50), 20)
     # set color of perimeter of shape
     shape.setOutline("red")
     # fill shape with color of your choosing
     shape.setFill("red")
     # draws the shape onto window
     shape.draw(win)
     # sets position of shape wherever you click the mouse on the window
     for i in range(5):
          # waits for user to click on window to define next point of shape or to close window
          p = win.getMouse()
          # returns a clone to center point of shape
          c = shape.getCenter()
          # getting the difference of original "x" point with the new "x" point
          dx = p.getX() - c.getX()
          # getting the difference of original "y" point with the new "y" point
          dy = p.getY() - c.getY()
          # moves the shape with the new coordinates
          shape.move(dx,dy)
          # closes the window
     win.close()

main()