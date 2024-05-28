n = int(input())
drinks = [int(x) for x in input().split(' ')]

total = 0
for i in range(n):
    total += drinks[i]/100

print((total/n)*100)