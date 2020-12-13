import sys

with open(sys.argv[1]) as input :
    min_time = int(input.readline())
    lines = (int(l) for l in input.readline().split(",") if not l == "x")
waits = {(l - min_time%l):l for l in lines}
min_wait = min(waits.keys())
print(min_wait, waits[min_wait], min_wait*waits[min_wait])
