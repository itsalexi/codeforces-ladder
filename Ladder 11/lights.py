inputGrid = []
grid =  [[1,1,1],[1,1,1], [1,1,1]]
for i in range(3):
    rowIn = [int(i) for i in input().split(' ')]
    rowOut = []
    for j in range(3):
        rowOut.append(rowIn[j] % 2)
    inputGrid.append(rowOut)
for i in range(3):
    for j in range(3):
        if inputGrid[i][j] == 1:
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = 1
            if i > 0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 0
                else:
                    grid[i-1][j] = 1 
            if i < 2:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 0
                else:
                    grid[i+1][j] = 1             
            if j > 0:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 0
                else:
                    grid[i][j-1] = 1               
            if j < 2:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 0
                else:
                    grid[i][j+1] = 1                
[print (*grid[x], sep="") for x in range(3)]