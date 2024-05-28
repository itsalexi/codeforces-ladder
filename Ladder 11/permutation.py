n = int(input())
answer = []

if n % 2 == 0:
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i+1)
        else:
            answer.append(i-1)
else:
    answer.append(-1)
    
print(*answer)