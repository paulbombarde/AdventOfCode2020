import sys
from collections import defaultdict,deque

graph = defaultdict(set)
with open(sys.argv[1]) as input :
    for l in input :
        w = l.split()
        out_color = " ".join(w[0:2])
        print(out_color)

        for i in range(5, len(w), 4) :
            color = " ".join(w[i:i+2])
            print(color)
            graph[color].add(out_color)
        print()

class Counter :
    def __init__(self):
        self.count = 0
        self.seen = set()
        self.bfs = deque()

    def check(self, color) :
        print(color, graph[color])
        for c in graph[color] :
            if c in self.seen :
                continue
            self.seen.add(c)
            self.bfs.append(c)
            self.count+=1

    def run(self, start) :
        self.bfs.clear()
        self.seen.clear()
        self.count = 0
        self.check(start)
        while self.bfs :
            next = self.bfs.popleft()
            self.seen.add(next)
            self.check(next)

counter = Counter()
counter.run("shiny gold")
print(counter.count)

