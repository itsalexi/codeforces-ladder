n = int(input())

found = False

while not found:
    n += 1
    n_list = list(map(int, str(n)))
    n_set = set(n_list)
    if len(n_list) == len(n_set):
        print(n)
        found = True