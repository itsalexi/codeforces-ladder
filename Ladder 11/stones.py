n = int(input())
colors = list(input())
r = 0
g = 0 
b = 0
for i in range(n):
    if colors[i] == 'r':
        r += 1
    elif colors[i] == 'g':
        g += 1
    elif colors[i] == 'b':
        b += 1

