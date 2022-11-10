import sys

strs = []
idx = 0

while True:

    strs.append(sys.stdin.readline().strip("\n"))

    if strs[idx] == "EOI":
        strs.pop()
        break

    idx += 1

for i in strs:

    if "nemo" in i.lower():
        print("Found")
    else:
        print("Missing")
