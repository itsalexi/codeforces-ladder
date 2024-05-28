n = int(input())
left_cupboards = []
right_cupboards = []
seconds = 0

for i in range(n):
    l, r = map(int, input().split())
    left_cupboards.append(l)
    right_cupboards.append(r)

if left_cupboards.count(0) > left_cupboards.count(1):
    seconds += abs(n - left_cupboards.count(0))
else:
    seconds += abs(n - left_cupboards.count(1))
    
if right_cupboards.count(0) > right_cupboards.count(1):
    seconds += abs(n - right_cupboards.count(0))
else:
    seconds += abs(n - right_cupboards.count(1))
    
print(seconds)