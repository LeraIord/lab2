import math 

class Vector:

    def __init__(v1, x, y, z):
        v1.x=x
        v1.y=y
        v1.z=z
   
    def __repr__(v1):
        return repr((v1.x, v1.y, v1.z))

    @property
    def getx(self):
        return self.x
        
    @property
    def gety(self):
        return self.y

    @property
    def getz(self):
        return self.z    



    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    def __sub__(v1, v2):
        return Vector(v1.x - v2.x, v1.y - v2.y , v1.z - v2.z)

    def __add__(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

    def __neg__(v1):
        return Vector((-1)*v1.x, (-1)*v1.y, (-1)*v1.z)
    
    def __product__(v1, value):
        return Vector(v1.x * value, v1.y * value, v1.z * value)

    def modulvector(v1):
        return math.sqrt(v1.x**2+v1.y**2+v1.z**2)  

    def  cross_product(v1,v2):
        return Vector(v1.y*v2.z-v1.z*v2.y, (-1)*(v1.x*v2.z-v1.z*v2.x), v1.x*v2.y-v1.y*v2.x)    



