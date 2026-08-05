class Person( object ):

        def __init__(self, name, idnumber):
                self.name = name
                self.idnumber = idnumber
        def display(self):
                print(self.name)
                print(self.idnumber)
                print(self.IQ)
                print(self.post)

class Student( Person ):
        def __init__(self, name, idnumber, IQ, post):
                self.IQ = IQ
                self.post = post 

                Person.__init__(self, name, idnumber)

I = Student('Badar',  862216, 100, "Intern")

I.display() 

