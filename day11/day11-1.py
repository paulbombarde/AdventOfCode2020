import sys

grid = [l.rstrip() for l in open(sys.argv[1])]
def next_state(i,j) :
    if grid[i][j] == "." :
        return "."

    n = 0
    if 0 < i :
        if 0 < j and grid[i-1][j-1] == "#" :
            n+=1
        if grid[i-1][j] == "#" :
            n+=1
        if j < len(grid[i])-1 and grid[i-1][j+1] == "#" :
            n+=1
    if i < len(grid)-1 :
        if 0 < j and grid[i+1][j-1] == "#" :
            n+=1
        if grid[i+1][j] == "#" :
            n+=1
        if j < len(grid[i])-1 and grid[i+1][j+1] == "#" :
            n+=1
    if 0 < j and grid[i][j-1] == "#" :
        n+=1
    if j < len(grid[i])-1 and grid[i][j+1] == "#" :
        n+=1

    if n == 0 and grid[i][j] == "L" :
        return "#"
    if 4 <= n and grid[i][j] == "#" :
        return "L"
    return grid[i][j]




changed = True
while changed :
    # too lazy to do it in place
    changed = False
    next_grid = []
    for i in range(len(grid)) :
        l = ""
        for j in range(len(grid[i])):
            n = next_state(i,j)
            if not n == grid[i][j] : changed = True
            l += n
        #print(l)
        next_grid.append(l)
    grid = next_grid
    #print()

count = 0
for l in grid :
    for c in l :
        if c == "#" :
            count += 1
print(count)


