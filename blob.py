import random


# tut 16

class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), movement_range=(-1, 2)):
        # when object is created, whatever is in init method is gonna run
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, x_boundary)
        self.y = random.randrange(0, y_boundary)
        self.movement_range = movement_range

    def __repr__(self):     # if I just call the object --> blue_blobs[2]
        return 'Blob({}, {}, ({}, {}))'.format(self.color, self.size, self.x, self.y)

    def __str__(self):      # if I use print(....) --> print(blue_blobs[2])
        return 'Blob of color:{}, size: {}, location: ({}, {})'.format(self.color, self.size, self.x, self.y)

    def move(self):
        self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary
        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary
