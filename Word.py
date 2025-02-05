word = input()
upper, lower = 0, 0
for i in word:
    if i.isupper():
        upper += 1
    else:
        lower += 1
    if upper > lower:
        print(word.upper())
    elif upper < lower:
        print(word.lower())
    else:
        print(word.lower())
