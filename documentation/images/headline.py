# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

# CONSTANTS
W = 1024  # Width
H = 160   # Height
M = 32    # Margin
U = 32    # Unit (Grid Unit)

# DRAWS A GRID
def grid():
    strokeWidth(1)
    stroke(0.5,0,0)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(32):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(8):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))
    fill(0.9)
    stroke(None)

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
new_page()
#grid() # Toggle for grid view

font("fonts/ttf/NewspaperText-Regular.ttf")
fontSize(M*4.5)
fill(1)
text("Newspaper Text", (M*0.7, M*1))

# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/images/headline.png")
print("[DrawBot]: Headline image updated")
