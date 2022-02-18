#!/usr/bin/python
import math

def displayPathtoPrincess(n,grid):
#print all the moves here
    numberOfMoves = math.floor(n/2)
    if grid[0][0] == 'p':
        for i in range(numberOfMoves):
            print ('UP')
        for i in range(numberOfMoves):
            print ('LEFT')
    elif grid[0][n-1] == 'p':
        for i in range(numberOfMoves):
            print ('UP')
        for i in range(numberOfMoves):
            print ('RIGHT')
    elif grid[n-1][0] == 'p':
        for i in range(numberOfMoves):
            print ('DOWN')
        for i in range(numberOfMoves):
            print ('LEFT')
    else:
        for i in range(numberOfMoves):
            print ('DOWN')
        for i in range(numberOfMoves):
            print ('RIGHT')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)