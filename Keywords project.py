#Take user input
a = input ("Enter a word: ")
#program to check break keyword
for i in a: #iterate for loop
  if (i == 'A'): #condition 1
  #display result
    print ("A is found") 
    break #break statement
  else:
  #display result
    print ("A not found")


for x in range(10): #iterate for loop
    if x % 20 == 0: #condition 1
       print("twist")

    elif x % 15 == 0: #condition 2
       pass       #pass statement

    elif x % 5 == 0: #condition 3
       print("fizz")   #display result

    elif x % 3 == 0:  #condition 4
       print("buzz")    #display result

    else:              #condition 5
       print(x)        #display result
    
    
var = 10           #initialise         
while var > 0:     #iterate loop         
   var = var - 1
   if var == 5:       #condition 1
      continue        #continue statement
      #display result
   print ('\nCurrent variable value :', var)
print ("\nGood bye!")

