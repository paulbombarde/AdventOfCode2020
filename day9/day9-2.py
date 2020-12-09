import sys
from collections import deque

previous25 = set()
numbers = []
ni=0
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
                invalid = i
            previous25.remove(numbers[ni])
            ni+=1
        numbers.append(i)
        previous25.add(i)

print("invalid :",invalid)

sum=numbers[0]
f=0
l=0
while not sum == invalid :
    if sum < invalid :
        l+=1
        sum += numbers[l]
    else :
        sum -= numbers[f]
        f+=1

sub = numbers[f:l+1]
print(sub)
mi = min(sub)
ma = max(sub)
print(mi, ma, mi+ma)

    
