import sys

with open(sys.argv[1]) as input :
    code = {l:c.rstrip() for (l,c) in enumerate(input)}

class Tester :
    def run(self) :
        self.seen = set()
        self.sp = 0
        self.acc = 0
        while not self.sp in self.seen :
            self.seen.add(self.sp)
            if not self.sp in code :
                return True
            
            c = code[self.sp]
            [action, value] = c.split()
            value = int(value)
            if action == "nop" :
                self.sp += 1
            elif action == "acc" :
                self.acc += value
                self.sp += 1
            elif action == "jmp" :
                self.sp += value
        return False

o = Tester()
o.run()

for l in o.seen :
    [action, value] = code[l].split()
    if action == "acc":
        continue
    if action == "nop" :
        code[l]="jmp "+value
    else :
        code[l]="nop "+value
    t = Tester()
    if t.run() :
        print(l, t.acc)
        #break
    code[l] = action+" "+value

