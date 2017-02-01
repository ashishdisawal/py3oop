class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p1 = Point()
p2 = Point()

p1.reset()
p2.reset()

print(p1.x, p1.y)
print(p2.x, p2.y)

p1.x = 2
p1.y = 3

p2.x = 4
p2.y = 1

print(p1.x, p1.y)
print(p2.x, p2.y)
