n, t = list(map(int, input().split(' ')))
queue = list(input())

for i in range(t):
    lastQueue = queue.copy()
    for j in range(n-1):
        if lastQueue[j] == 'B' and lastQueue[j+1] == 'G':
            queue[j] = 'G'
            queue[j+1] = 'B'
print (*queue, sep='')
