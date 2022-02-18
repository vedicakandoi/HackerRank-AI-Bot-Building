#

def nextMove(n,r,c,grid):
    for row in grid:
        if 'p' in row:
            pc = row.index('p')
            pr = grid.index(row)
    if r > pr:
        return ("UP")
    elif r < pr:
        return ("DOWN")
    elif c > pc:
        return ("LEFT")
    else:
        return ("RIGHT")
                
            

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))