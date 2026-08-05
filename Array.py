import array as arr

array_num = arr.array('i', [1, 3, 5, 2, 8, 3, 6, 7])
print("Original array: "+str(array_num))

print("Numbaer of occurrences if the number 3 in the said array: "+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num)) 