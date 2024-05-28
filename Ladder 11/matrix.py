for i in range(5):
    row = [int(i) for i in input().split(' ')]
    for j in range(5):
        if row[j] == 1:
            print(abs(2 - i)+abs(2 - j))
            break

