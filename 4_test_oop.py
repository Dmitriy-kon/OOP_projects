class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self.validate_coordinate(x):
            self.__x = x
        else:
            self.__x = 0

        if self.validate_coordinate(y):
            self.__y = y
        else:
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if self.validate_coordinate(new_x):
            self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if self.validate_coordinate(new_y):
            self.__y = new_y

    @classmethod
    def validate_coordinate(cls, data):
        return type(data) in {int, float} and cls.MIN_COORD <= data <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2


vec = RadiusVector2D(2, 4)
print(vec.y)
vec.y = 1050
print(vec.y)
print(RadiusVector2D.norm2(vec))
