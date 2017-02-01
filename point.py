import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y


    def reset(self):
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        return math.sqrt(
                (self.x - other_point.x)**2 +
                (self.y - other_point.y)**2)

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

print("Distance between p1 and p2: {}".format(p1.calculate_distance(p2)))
assert (p1.calculate_distance(p2) == p2.calculate_distance(p1))
