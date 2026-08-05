L = [4, 5, 3, 4, 6, 2, 5, 8, 0]
print("Original List :", L)

count = 0

for i in L:
    count += 1

avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

L.sort()

print("Smallest element is:", L[0])

print("Largest element is:", L[-1])