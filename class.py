import math as m
class Point:
    def move(self, x, y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return m.sqrt(
            (self.x-other_point.x)**2 +
            (self.y-other_point.y)**2
        )
    
p1=Point()
p2=Point()
p1.reset()
p2.move(5,0)
print(p2.calculate_distance(p1))
#assert is used as a siple test tool
#The program bails if the code after it is either false, none or empty
assert(
    p1.calculate_distance(p2)==
    p2.calculate_distance(p1)
)

p1.move(3,4)
print(p1.calculate_distance(p2))