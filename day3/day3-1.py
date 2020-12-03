import sys

with open(sys.argv[1]) as input :
    c=0
    i=0
    it=iter(enumerate(input))
    N=len(next(it)[1])-1 # don't care for the first row

    for j,l in it :
        i+=3
        i=i%N
        # print(j, l, i, N, l[i])
        if l[i]=='#' : c+=1

    print(c)
