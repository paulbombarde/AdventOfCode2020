#input = "389125467"
input = "198753462"
nb_moves = 10000000

min_label = 1
max_label = 1000000
labels = [i+1 for i in range(max_label+1)]
inputs = [int(i) for i in input]
for i in range(len(input)-1) :
    labels[inputs[i]]=inputs[i+1]
labels[inputs[8]]=10
labels[max_label]=inputs[0]
#labels[inputs[8]]=inputs[0]

def select_next(v) :
    target =v - 1
    if target < min_label :
        target = max_label
    return target

current = inputs[0]
def str_cup(n):
    if n == current :
        return "("+str(n)+") "
    else:
        return str(n)+" "

def str_cups():
    r=str_cup(1)
    n = labels[1]
    while not n == 1 :
        r+=str_cup(n)
        n = labels[n]
    return r

for i in range(nb_moves) :
    pick_up = [labels[current], labels[labels[current]], labels[labels[labels[current]]]]
    target = select_next(current)
    while target in pick_up :
        target = select_next(target)

    o = labels[pick_up[2]]
    labels[current]=o
    t = labels[target]
    labels[target] = pick_up[0]
    labels[pick_up[2]]=t
    current = labels[current]

print("-- final --")
print(labels[1], labels[labels[1]], labels[1]*labels[labels[1]])

