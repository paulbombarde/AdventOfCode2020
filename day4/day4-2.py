import sys
import re

hcl_re = re.compile("#[0-9a-f]{6}")
expected_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
class Id :
    def __init__(self):
        self.d={}

    def parse(self,l) :
        kvs = (kv.split(':') for kv in l.split())
        self.d.update({kv[0]:kv[1] for kv in kvs})

    def check(self) :
        print("\n", self.d)
        r = expected_keys.intersection(self.d.keys())
        if len(r) < len(expected_keys):
            print("missing keys")
            return False


        byr = int(self.d["byr"])
        if byr < 1920 or 2002 < byr :
            print("invalid byr", byr)
            return False
        
        iyr = int(self.d["iyr"])
        if iyr < 2010 or 2020 < iyr :
            print("invalid iyr", iyr)
            return False

        eyr = int(self.d["eyr"])
        if eyr < 2020 or 2030 < eyr :
            print("invalid eyr", eyr)
            return False

        hgt = self.d["hgt"]
        if hgt.endswith("in") :
            h = int(hgt[:-2])
            if h < 59 or 76 < h :
                print("invalid hgt", hgt, h)
                return False
        elif hgt.endswith("cm") :
            h = int(hgt[:-2])
            if h < 150 or 193 < h :
                print("invalid hgt", hgt, h)
                return False
        else :
            print("invalid hgt", hgt)
            return False

        hcl = self.d["hcl"]
        if not hcl_re.match(hcl) :
            print("invalid hcl", hcl)
            return False

        ecl = self.d["ecl"]
        if not ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} :
            print("invalid ecl", ecl)
            return False

        pid = self.d["pid"]
        if not len(pid) == 9 :
            print("invalid pid", pid)
            return False
        p = int(pid)
        return True


with open(sys.argv[1]) as input:
    count = 0
    full_count = 0
    id = Id()
    for l in input :
        if 1 < len(l):
            id.parse(l)
        else :
            full_count += 1
            res = False
            try :
                res = id.check()
            except Exception as e :
                print(e)
                pass
            if res :
                count += 1
            print(res)
            id.d.clear()

    if len(id.d):
            full_count += 1
            res = False
            try :
                res = id.check()
            except Exception as e :
                print(e)
                pass
            if res :
                count += 1
            print(res)

    print(count, full_count, sep='/')
