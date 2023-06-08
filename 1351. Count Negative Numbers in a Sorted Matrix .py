grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

def countNegatives(grid):
    count = 0
    for l in grid:
        for i in range(len(l)):
            if l[i] <= 0:
                count += 1

    return count

print(countNegatives(grid))
