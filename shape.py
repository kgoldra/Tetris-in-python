class Shape():
    shapes = [
        "straight",
        "box",
    ]

    def __init__(self, shape):
        self.x = 5
        self.y = 0


        if shape == 'straight':
            self.color = 1
            self.shape = [[1],
                          [1],
                          [1],
                          [1]]
            self.height = len(self.shape)
            self.width = len(self.shape[0])

        elif shape == 'box':
            self.color = 4
            self.shape = [[1, 1],
                          [1, 1]]
            self.height = len(self.shape)
            self.width = len(self.shape[0])




    def move_left(self, grid):
        if self.x > 0:
            count = 0
            for y in range(self.height):
                if grid[self.y + y][self.x - 1] == 0:
                    count += 1
            if count == self.height:
                for y in range(self.height):
                    for x in range(self.width):
                        grid[self.y + y][self.x + x] = 0
                self.x -= 1


    def move_right(self, grid):
        if self.x + self.width - 1 < 11:
            count = 0
            for y in range(self.height):
                if grid[self.y + y][self.x + self.width] == 0:
                    count += 1
            if count == self.height:
                for y in range(self.height):
                    for x in range(self.width):
                        grid[self.y + y][self.x + x] = 0
                self.x += 1
                print("moving right")

#a bit buggy but work
    def rotation(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                grid[self.y + y][self.x + x] = 0

        temp = self.height
        self.height = self.width
        self.width = temp

        for y in range(self.height):
            for x in range(self.width):
                grid[self.y + y][self.x + x] = self.color

#someting wrong here
    def move_bot(self, grid):
        boty = 22
        while grid[boty][self.x] != 0:
            boty -= 1
            print(boty)
        grid[self.y][self.x] = 0
        self.y = boty
        grid[self.y][self.x] = self.color


# function to move the block down if theres nothing below after a section is cleared
def row_gravity():
    for y in range(23, 0, -1):
        count = 0
        for x in range(12):
            if grid[y][x] == 0:
                count += 1
            if count == 12:
                for xtemp in range(12):
                    grid[y][xtemp] = grid[y - 1][xtemp]
                    grid[y - 1][xtemp] = 0


# function for clearing row
def row_clear():
    for y in range(23, -1, -1):
        count = 0
        for x in grid[y]:
            if x != 0:
                count += 1
            if count == 12:
                for xtemp in range(12):
                    grid[y][xtemp] = 0
    row_gravity()





grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
