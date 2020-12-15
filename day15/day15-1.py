from collections import defaultdict

last = {}
input = [0,6,1,7,2,19,20]
max_turn = 2020
#input = [0,3,6]
#max_turn = 10
turn = 1
for i in input :
    last[i]=turn
    print("---",turn, i)
    turn += 1

next_spoken = last[input[-1]] - turn +1
while turn <= max_turn :
    spoken = next_spoken
    print("---",turn, spoken)
    if spoken in last :
        #print("last", last[spoken])
        next_spoken = turn - last[spoken]
    else:
        #print("new")
        next_spoken = 0
    last[spoken] = turn
    #print("next", next_spoken)
    turn+=1

