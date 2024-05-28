numbers = list(map(int, list(str(input()))))

lucky_numbers = 0
for i in range(len(numbers)):
    if numbers[i] == 7 or numbers[i] == 4:
        lucky_numbers += 1

if lucky_numbers == 7 or lucky_numbers == 4:
    print("YES")
else:
    print("NO")