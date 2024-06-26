n = int(input())

passengers = 0
stops = []

for i in range(n):
    leave, enter = map(int, input(' ').split(' '))
    passengers += enter - leave
    stops.append(passengers)
    
print(max(stops))