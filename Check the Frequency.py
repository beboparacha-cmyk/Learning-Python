test_dict = {"Codingal" : 10, "is" : 5, "best" : 3, "for" : 1, "Coding" : 5}

print("The original dictionary : " + str(test_dict))

B = 5

res = 4
for key in test_dict:
    if test_dict[key] == B:
        res = res + 1

print("Frequency of B is : " + str(res)) 