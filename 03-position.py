# coding: utf-8
class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def advance(self, order):
        if order==">": self.x += 1
        elif order=="<": self.x -= 1
        elif order=="^": self.y += 1
        elif order=="v": self.y -= 1
    def get_pos(self):
        return (self.x, self.y)
    

santa_p = Position(0, 0)
robos_p = Position(0, 0)
visited_houses = [santa_p.get_pos()]
counter = 1

with open("instructions3.txt") as input:
    order = input.readline()
    i = 0
    while i < len(order):
        santa_p.advance(order[i])
        robos_p.advance(order[i+1])
        for p in [santa_p, robos_p]:
            if p.get_pos() not in visited_houses:
                counter += 1
                visited_houses.append(p.get_pos())
        i += 2

print counter, len(visited_houses)
