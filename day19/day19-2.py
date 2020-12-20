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

def patch_rules():
    rules[8] = [['42'],['42','8']]
    rules[11]= [['42','31'],['42','11','31']]

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
    input = [
'42: 9 14 | 10 1',
'9: 14 27 | 1 26',
'10: 23 14 | 28 1',
'1: "a"',
'11: 42 31',
'5: 1 14 | 15 1',
'19: 14 1 | 14 14',
'12: 24 14 | 19 1',
'16: 15 1 | 14 14',
'31: 14 17 | 1 13',
'6: 14 14 | 1 14',
'2: 1 24 | 14 4',
'0: 8 11',
'13: 14 3 | 1 12',
'15: 1 | 14',
'17: 14 2 | 1 7',
'23: 25 1 | 22 14',
'28: 16 1',
'4: 1 1',
'20: 14 14 | 1 15',
'3: 5 14 | 16 1',
'27: 1 6 | 14 18',
'14: "b"',
'21: 14 1 | 1 14',
'25: 1 1 | 1 14',
'22: 14 14',
'8: 42',
'26: 14 22 | 1 20',
'18: 15 15',
'7: 14 5 | 1 21',
'24: 14 1']

    read_rules(input)

    lines = [
'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
'bbabbbbaabaabba',
'babbbbaabbbbbabbbbbbaabaaabaaa',
'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
'bbbbbbbaaaabbbbaaabbabaaa',
'bbbababbbbaaaaaaaabbababaaababaabab',
'ababaaaaaabaaab',
'ababaaaaabbbaba',
'baabbaaaabbaaaababbaababb',
'abbbbabbbbaaaababbbbbbaaaababb',
'aaaaabbaabaaaaababaa',
'aaaabbaaaabbaaa',
'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
'babaaabbbaaabaababbaabababaaab',
'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba']

    for l in lines :
        print(l, matches(l))
    print(count_matches(lines))
    patch_rules()

    print("After patch")
    for l in lines :
        print(l, matches(l))
    print(count_matches(lines))

else :
    with open(sys.argv[1]) as input :
        it = iter(input)
        read_rules(it)
        patch_rules()
        print(count_matches(it))






            


