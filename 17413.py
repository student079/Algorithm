import sys

item = sys.stdin.readline().strip("\n")

tag = False

result = []
temp = []

for i in item:
    if i == "<":
        tag = True
        if len(temp) != 0:
            result.append(temp[::-1])
            temp.clear()
        result.append(i)
        continue
    elif i == ">":
        tag = False
        result.append(i)
        continue
    elif i == " ":
        if tag:
            result.append(i)
        else:
            result.append(temp[::-1])
            temp.clear()
            result.append(i)

        continue

    if tag:
        result.append(i)
    else:
        temp.append(i)
else:
    result.append(temp[::-1])
    temp.clear()

for i in result:
    print("".join(i), end="")
