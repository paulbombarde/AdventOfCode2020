import sys

grid = [l.rstrip() for l in open(sys.argv[1])]
def look_in_dir(i, j, di, dj) :
    i = i-di
    j = j-dj
    while 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0]) and grid[i][j] == "." :
        i = i-di
        j = j-dj
    if i<0 or len(grid)<=i or j<0 or len(grid[0])<= j :
        return "."
    return grid[i][j]

def next_state(i0,j0) :
    if grid[i][j] == "." :
        return "."

    n = 0
    if "#" == look_in_dir(i,j,-1,-1) :
        n+=1
    if "#" == look_in_dir(i,j,-1,0) :
        n+=1
    if "#" == look_in_dir(i,j,-1,1) :
        n+=1
    if "#" == look_in_dir(i,j,0,-1) :
        n+=1
    if "#" == look_in_dir(i,j,0,1) :
        n+=1
    if "#" == look_in_dir(i,j,1,-1) :
        n+=1
    if "#" == look_in_dir(i,j,1,0) :
        n+=1
    if "#" == look_in_dir(i,j,1,1) :
        n+=1

    if n == 0 and grid[i][j] == "L" :
        return "#"
    if 5 <= n and grid[i][j] == "#" :
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


