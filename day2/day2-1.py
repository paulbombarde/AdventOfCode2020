import sys

def check(line) :
    s = line.split();
    letter = s[1][0]
    pwd = s[2]
    s = s[0].split('-')
    low = int(s[0])
    high = int(s[1])

    c = 0
    for l in pwd :
        if l == letter :
            c+=1
    res = (low <= c) and (c <= high)
    #print(letter, low, high, c, pwd, res)
    return res

with open(sys.argv[1]) as input :
    count = 0
    for l in input :
        if check(l) :
            count += 1
    print(count)

