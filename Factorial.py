def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''

    if x==0 or x==1:
     return 1
    else:
     return x*factorial(x-1)
    
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 2:",factorial(2))
print("the factorial of 10:",factorial(10))
print("the factorial of 50:",factorial(50))
print("the factorial of 30:",factorial(30))
print("the factorial of 13:",factorial(13))
print("the factorial of 456:",factorial(456))