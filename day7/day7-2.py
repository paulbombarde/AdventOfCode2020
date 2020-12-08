import sys
from collections import defaultdict,deque

graph = defaultdict(list)
with open(sys.argv[1]) as input :
    for l in input :
        w = l.split()
        out_color = " ".join(w[0:2])

        for i in range(4, len(w), 4) :
            if w[i] == "no" :
                continue
            nb = int(w[i])
            color = " ".join(w[i+1:i+3])
            graph[out_color].append((nb, color))
        #print(out_color, graph[out_color])

count = 0
bfs = deque()
bfs.append((1,"shiny gold"))
while bfs :
    nnext, next = bfs.popleft()
    print(nnext, next, graph[next])
    for n,c in graph[next]:
        count += n*nnext
        bfs.append((n*nnext, c))

print(count)

