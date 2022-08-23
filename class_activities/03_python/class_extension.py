class Square:
    def __init__(self, 
                 side_length:float,
                 origin_point = (0,0)) -> None:
        self.l = side_length
        self.ox = origin_point[0]
        self.oy = origin_point[1]
        self.origin = origin_point
    
    def perimeter(self) -> float:
        return 4 * self.l
    
    def area(self) -> float:
        return self.l ** 2
    
    def displace(self, x:float = 0, y:float = 0):
        self.ox += x
        self.oy += y
        self.origin = (self.ox, self.oy)

    def scale(self, scale:float):
        self.l *= scale

class Cube(Square):
    def __init__(self,
                 side_length:float,
                 origin_point = (0,0,0)) -> None:

        super().__init__(side_length=side_length,origin_point=origin_point[:2])
        self.oz = origin_point[2]
        self.origin = origin_point
    
    def face_area(self):
        return super().area()
    
    def area(self):
        return super().area() * 6
    
    def volume(self):
        return self.l ** 3

    def displace(self, x:float = 0, y:float = 0, z:float = 0):
        super().displace(x,y)
        self.oz += z
        self.origin = (self.ox, self.oy, self.oz)