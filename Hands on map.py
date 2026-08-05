number10 = [10, 20, 30, 40, 50]
number7 = [7, 14, 21, 28, 35]
result = map(lambda x, y: x + y, number10, number7)
print("Addition of two lists:")
print(list(result))

nums = [1, 2, 10, 7, 8, 14, 9]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in list:")
print(square) 