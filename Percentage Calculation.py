 # take marks as input from user
print("Enter Marks Obtained in 6 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
history = int(input("history :"))
geography = int(input("geography :"))
urdu = int(input("urdu: "))

# Let's calculate the percentage of marks
sum = math+english+science+history+geography+urdu
print("sum of math,english,science,history,geography and urdu")

percentage = (sum/600)*100

print(end="Percentage Mark = ")
print(percentage)