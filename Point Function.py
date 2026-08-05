class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "({1},{1})".format(self.__x, self.__y)
    
p1 = Point(10, 90)
print(p1) 



class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "({0},{0})".format(self.__x, self.__y)
    
p2 = Point(100, 900)
print(p2) 




class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "({0},{1})".format(self.__x, self.__y)
    
p3 = Point(1000, 9000)
print(p3) 





class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "({1},{0})".format(self.__x, self.__y)
    
p4 = Point(10000, 90000)
print(p4) 







class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "({1},{0})".format(self.__x, self.__y)
    
p5 = Point(100000, 900000)
print(p5)  
