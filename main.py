import turtle
from shape import *
import random

mw = turtle.Screen()
mw.title("Tetris")
mw.bgcolor("black")
mw.setup(width=600, height=800)
mw.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

shapes = Shape.shapes

shape_chosen = shapes[random.randint(0, 1)]



def draw_grid(pen, grid):
    pen.clear()
    starty = 230
    startx = -110

    colors = ["white",
              "cyan",
              "blue",
              "pink",
              "orange",
              "green",
              "purple",
              "red"]


    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = startx + (x * 20)
            screen_y = starty - (y * 20)

            color = colors[grid[y][x]]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


# shape creation
shape = Shape(shape_chosen)

#putting the shape in the grid
grid[shape.y][shape.x] = shape.color

#drawing the initial grid
draw_grid(pen, grid)



mw.listen()
mw.onkey(lambda: shape.move_left(grid), "a")
mw.onkey(lambda: shape.move_right(grid), "d")
mw.onkey(lambda: shape.move_bot(grid), "s")
mw.onkey(lambda: shape.rotation(grid), "space")

#main game loop
while True:
    mw.update()

    #creating new shape when there's nowhere to move below
    if shape.y == 23 - shape.height + 1 or grid[shape.y + shape.height][shape.x] != 0 or grid[shape.y + shape.height][shape.x + shape.width - 1] != 0:
        shape.y = 0
        shape_chosen = shapes[random.randint(0, 1)]
        shape = Shape(shape_chosen)
        row_clear()

#something wrong below (couldn't spawn block at 0 y = 0)
    #shape movement to the bottom
    elif grid[shape.y + shape.height][shape.x] == 0:
        if shape.y + 1 < 23:

            for y in range(shape.height):
                for x in range(shape.width):
                    grid[shape.y + y][shape.x + x] = 0

            shape.y += 1

            for y in range(shape.height):
                for x in range(shape.width):
                    grid[shape.y + y][shape.x + x] = shape.color

    draw_grid(pen, grid)

mw.mainloop()
