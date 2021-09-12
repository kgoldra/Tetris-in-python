import turtle
from shape import *

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


def draw_grid(pen, grid):
    pen.clear()
    starty = 230
    startx = -110

    colors = ["white",
              "cyan",
              "blue",
              "orange",
              "yellow",
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
shape = Shape()

#putting the shape in the grid
grid[shape.y][shape.x] = shape.color

#drawing the initial grid
draw_grid(pen, grid)



mw.listen()
mw.onkey(lambda: shape.move_left(grid), "a")
mw.onkey(lambda: shape.move_right(grid), "d")
mw.onkey(lambda: shape.move_bot(grid), "s")

#main game loop
while True:
    mw.update()

    #creating new shape when there's nowhere to move below
    if shape.y == 23 - shape.height + 1 or grid[shape.y + shape.height][shape.x] != 0:
        shape.y = 0
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
#            grid[shape.y][shape.x] = shape.color
#            grid[shape.y-1][shape.x] = 0


#        elif shape.y+1 == 23:
#            shape.y += 1
#            grid[shape.y][shape.x] = shape.color
#            grid[shape.y - 1][shape.x] = 0


    draw_grid(pen, grid)

mw.mainloop()
