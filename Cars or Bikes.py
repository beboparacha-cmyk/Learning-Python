print("Select your ride: ")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice: "))
if( choice == 1):
    print(" what type of bike? ")
    print(" 1. BMW S 1000 RR\n")
    print(" 2. Giant Bicycle\n")

    choice2=int(input("Enter your choice2: "))
    if choice2 ==1:
        print("you have selected BMW S 1000 RR")
    else:
        print("you have selected Giant Bicycle")

elif(choice == 2):
    print(" what type of car?")
    print("1. lexus LC")
    print("2. Porshe 718 Cayman")
    choice3=int(input("Enter your choice3: "))

    if choice3 ==1:
        print("you have selected Lexus LC")
    else:
        print("you have selected Porshe 718 Cayman")

else:
    print("Wrong choice!")