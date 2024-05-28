word = input()
letters = list(word)
upper_case = 0
lower_case = 0
for i in range (len(letters)):
    if letters[i].isupper():
        upper_case += 1
    else:
        lower_case += 1
if upper_case > lower_case:
    print(word.upper())
elif upper_case == lower_case:
    print(word.lower())
else:
    print(word.lower())