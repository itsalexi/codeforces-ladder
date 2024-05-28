encoded = list(input())

index = 0
decoded = []
while index != len(encoded):
    if encoded[index] == '-':
        if encoded[index + 1] == '.':
            decoded.append(1)
            index += 2 
        elif encoded[index + 1] == '-':
            decoded.append(2)
            index += 2 
    else:
        decoded.append(0)
        index += 1
print (*decoded, sep='')
