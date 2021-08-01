import math

class vec3():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def squared_length(self):
        return self.x**2+self.y**2+self.z**2

    def __add__(self, v):
        return vec3(self.x+v.x, self.y+v.y, self.z+v.z)

    def __sub__(self, v):
        return vec3(self.x-v.x, self.y-v.y, self.z-v.z)

    def mul(self, v):
        return vec3(self.x*v.x, self.y*v.y, self.z*v.z)

    
    def __mul__(self, a):
        return vec3(self.x*a, self.y*a, self.z*a)
    

    def div(self, v):
        return vec3(self.x/v.x, self.y/v.y, self.z/v.z)

    
    def __truediv__(self, a):
        return vec3(self.x/a, self.y/a, self.z/a)
    

    def dot(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z

    def cross(self, v):
        return vec3(self.y*v.z-self.z*v.y, self.z*v.x-self.x*v.z, self.x*v.y-self.y*v.x)

    def unit_vec(self):
        return self/self.length()

    def make_list(self):
        return [self.x, self.y, self.z]

    def printval(self):
        print((self.x, self.y, self.z))

class ray():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def origin(self):
        return self.a

    def direction(self):
        return self.b

    def point_at_parameter(self, t):
        return self.a + self.b*t

    def printval(self):      
        s0 = str(self.a.tuple())
        s1 = str(self.b.tuple())
        print('{0} + t{1}'.format(s0, s1))


def dot(a, b):
    return (a.x*b.x + a.y*b.y + a.z*b.z)