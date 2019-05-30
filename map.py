class A:

    mymap = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
]

    x = 0
    y = 0

    def position(self):

        for y, value_y in enumerate(self.mymap):
            for x, value_x in enumerate(value_y):
                if value_x == 1:
                    self.x = x
                    self.y = y
                    return self.y, self.x

    def right(self):
        try:
            self.mymap[self.y][self.x] = 0
            self.mymap[self.y][self.x+1] = 1
            self.x += 1
            return self.mymap
        except IndexError:
            self.mymap[self.y][0] = 1
            return self.mymap

    def left(self):
        try:
            self.mymap[self.y][self.x] = 0
            self.mymap[self.y][self.x - 1] = 1
            self.x -= 1
            return self.mymap
        except IndexError:
            self.mymap[self.y][len(self.x)] = 1
            return self.mymap

    def up(self):
        try:
            self.mymap[self.y][self.x] = 0
            self.mymap[self.y-1][self.x] = 1
            self.y -= 1
            return self.mymap
        except IndexError:
            self.mymap[-1][self.x] = 1
            return self.mymap

    def down(self):
        try:
            self.mymap[self.y][self.x] = 0
            self.mymap[self.y + 1][self.x] = 1
            self.y += 1
            return self.mymap
        except IndexError:
            self.mymap[0][self.x] = 1
            return self.mymap


a = A()
a.position()
print(a.up())
print(a.right())
