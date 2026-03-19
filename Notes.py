Amount =int(input("Please Enter Amount for Withdraw :"))

 # Calculating the number of nates of different denominations
note_1 = Amount//1050
note_2 = (Amount%1050)//500
note_3 = ((Amount%1050)%500)//100
note_4 = (((Amount%1050)%500)%100)//50


print("notes of 1050 rupee" , note_1)
print("notes of 500 rupee" , note_2)
print("notes of 100 rupee" , note_3)
print("notes of 50 rupee" , note_4)