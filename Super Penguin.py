class Bird:

    def __init__(self):
        print("Bird is ready!")

    def whoisThis(self):
        print("I am THE BIRD!!")

    def swim(self):
        print("I can swim faster..")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is READY!")

    def whoisThis(self):
        print("I am THE PENGUIN!!")

    def run(self):
        print("I can run faster..")

HarshFear = Penguin()
HarshFear. whoisThis()
HarshFear.swim()
HarshFear.run() 