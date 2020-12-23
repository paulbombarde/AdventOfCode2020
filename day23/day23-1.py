#input = "389125467"
#nb_moves = 10
input = "198753462"
nb_moves = 100

labels = [int(c) for c in input]
max_label = max(labels)
min_label = min(labels)

def select_next(v) :
    target =v - 1
    if target < min_label :
        target = max_label
    return target

for i in range(nb_moves) :
    print("-- move",i+1,"--")
    print("cups:", " ".join(str(c) for c in labels))
    pick_up = labels[1:4]
    print("pick up:", " ".join(str(c) for c in pick_up))
    target = select_next(labels[0])
    while target in pick_up :
        target = select_next(target)

    for j in range(4,len(labels)) :
        if labels[j]==target :
            # do stuff
            print("target pos:",j)
            labels = labels[4:j+1]+pick_up+labels[j+1:]+[labels[0]]
            break

print("-- final --")
print("cups:", " ".join(str(c) for c in labels))
i= labels.index(1)
r = "".join(str(c) for c in labels[i+1:])+"".join(str(c) for c in labels[:i])
print(r)

