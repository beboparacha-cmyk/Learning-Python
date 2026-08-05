class Computer:

    def __init__(self):
        self.__maxprice = 11000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()

bc = Computer()
bc.sell()

bc.__maxprice = 90000
bc.sell()

bc.setMaxPrice(90000)
bc.sell() 

cc = Computer() 
cc.sell()

cc.__maxprice = 1
cc.sell()

cc.setMaxPrice(1)
cc.sell() 