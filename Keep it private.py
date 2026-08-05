class myClass:

    __privateVar = 10;

    def __privateMeth(self):
        print("Don't tell anyone!!...IM A HUMAN...")

    def hello(self):
        print("The Private Variable value is: ",myClass.__privateVar)

Goo = myClass()
Goo.hello()
Goo._myClass__privateMeth   