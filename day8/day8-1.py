import sys

with open(sys.argv[1]) as input :
    code = {l:c.rstrip() for (l,c) in enumerate(input)}

seen = set()
sp = 0
acc = 0
while not sp in seen :
    seen.add(sp)
    c = code[sp]
    [action, value] = c.split()
    value = int(value)
    if action == "nop" :
        sp += 1
    elif action == "acc" :
        acc += value
        sp += 1
    elif action == "jmp" :
        sp += value

print(acc)

