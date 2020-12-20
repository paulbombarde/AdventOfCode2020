import sys
from collections import deque

rules = {}

def read_rules(it):
    # consume all rules
    for l in it :
        if len(l) == 1 :
            break
        [num, rule]=l.split(":")
        rules[int(num)]=[r.split() for r in rule.strip().split("|")]

def matches(l):
    l=l.strip()
    bfs = deque()
    bfs.append((0, [0]))
    while bfs :
        step = bfs.popleft()
        #print(step)
        i = step[0]
        first_rules_id, *other_rules = step[1]
        for rule in rules[first_rules_id]:
            #print("  ",rule)
            if rule[0][0] == '"' : # letter
                if not l[i] == rule[0][1] :
                    continue
                if i == len(l)-1 :
                    if not other_rules :
                        return True
                    continue
                if other_rules:
                    bfs.append((i+1,other_rules))
            else : 
                rule_int = [int(e) for e in rule]
                bfs.append((i, rule_int + other_rules))
    return False

def count_matches(it):
    return sum((1 for l in it if matches(l)))

#test = True
test = False 
if test :
    input = ['0: 4 1 5',
             '1: 2 3 | 3 2',
             '2: 4 4 | 5 5',
             '3: 4 5 | 5 4',
             '4: "a"',
             '5: "b""']
    read_rules(input)
    lines = ['ababbb\n',
             'bababa',
             'abbbab',
             'aaabbb',
             'aaaabbb']
    for l in lines :
        print(l, matches(l))
    print(count_matches(lines))

else :
    with open(sys.argv[1]) as input :
        it = iter(input)
        read_rules(it)
        print(count_matches(it))






            


