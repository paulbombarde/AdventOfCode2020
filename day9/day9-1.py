import sys
from collections import deque

previous25 = set()
numbers = deque()
with open(sys.argv[1]) as input :
    for l in input :
        i=int(l)
        if 25 <= len(numbers) :
            found = False
            for j in previous25 :
                if i-j in previous25 :
                    found = True
                    break
            if not found :
                print(i)
            previous25.remove(numbers.pop())
        numbers.appendleft(i)
        previous25.add(i)
            
    
