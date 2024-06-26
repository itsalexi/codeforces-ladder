equation = [int(factor) for factor in list(input('')) if factor != '+']
equation.sort()
print(*equation, sep="+")