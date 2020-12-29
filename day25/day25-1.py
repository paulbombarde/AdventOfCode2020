import sys

keys=[int(l) for l in open(sys.argv[1])]

subject_number = 7
divisor = 20201227
public_keys=[1]
def get_public_key(i) :
    while len(public_keys) <= i :
        #if len(public_keys)%10000 == 0 : print(len(public_keys), public_keys[-1], flush = True)
        v = public_keys[-1]*subject_number
        public_keys.append(v%divisor)
    return public_keys[i]

loop_sizes=[]
for k in keys :
    i = 0
    while get_public_key(i) != k :
        i+=1
    loop_sizes.append(i)

print(keys)
print(loop_sizes)

if loop_sizes[0] < loop_sizes[1] :
    subject_number=keys[1]
    public_keys=[1]
    print(get_public_key(loop_sizes[0]))
else:
    subject_number=keys[0]
    public_keys=[1]
    print(get_public_key(loop_sizes[1]))
