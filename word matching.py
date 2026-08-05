def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same\n", lst)
    return ctr

count = match_words(['abs', 'cfc', 'xyz', 'aba', '1221', 'appuana'])
print("Number of word having first and last character same:", count)