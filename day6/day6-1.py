import sys

with open(sys.argv[1]) as input :
    count = 0
    group = set()
    gl = []
    for l in input :
        l = l.rstrip()
        if len(l) == 0 :
            count += len(group)
            print(gl,group,len(group), count)
            group.clear()
            gl.clear()
        else:
            group.update(l)
            gl.append(l)
    count += len(group)
    print(gl,group,len(group), count)



