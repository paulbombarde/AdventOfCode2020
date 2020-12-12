import sys

i = 0
j = 0
wi = 1
wj = 10

for l in open(sys.argv[1]) :
    a = l[0]
    v = int(l[1:])
    print(a, v)

    if a == "F" :
        i += v*wi
        j += v*wj
    elif a == "N" :
        wi+=v
    elif a == "S" :
        wi-=v
    elif a == "E" :
        wj+=v
    elif a == "W" :
        wj-=v
    elif a == "R" :
        while v :
            t = wj
            wj = wi
            wi = -t
            v -= 90
    elif a == "L" :
        while v :
            t = wj
            wj = -wi
            wi = t
            v -= 90

    print(wi, wj, i, j)
print(abs(i)+abs(j))
