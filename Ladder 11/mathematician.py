first_pair = list(map(int,list(input(''))))
second_pair = list(map(int,list(input(''))))

answer = []

for i in range(len(first_pair)):
    if first_pair[i] == second_pair[i]:
        answer.append(0)
    else:
        answer.append(1)
print(*answer, sep='')