n = int(input())
x_positions = []
y_positions = []
z_positions = []

for i in range(n):
    x, y, z = list(map(int, input().split()))
    x_positions.append(x)
    y_positions.append(y)
    z_positions.append(z)

if sum(x_positions) == 0 and sum(y_positions) == 0 and sum(z_positions) == 0:
    print('YES')
else:
    print('NO')