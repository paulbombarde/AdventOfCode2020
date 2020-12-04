import sys

expected_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
class Id :
    def __init__(self):
        self.d={}

    def parse(self,l) :
        kvs = (kv.split(':') for kv in l.split())
        self.d.update({kv[0]:kv[1] for kv in kvs})

    def check(self) :
        r = expected_keys.intersection(self.d.keys())
        res = len(expected_keys) <= len(r)
        #print(r, res)
        return res


with open(sys.argv[1]) as input:
    count = 0
    full_count = 0
    id = Id()
    for l in input :
        if 1 < len(l):
            id.parse(l)
        else :
            full_count += 1
            if id.check() :
                count += 1
            id.d.clear()
    if len(id.d):
        full_count += 1
        if id.check() :
            count += 1

    print(count, full_count, sep='/')
