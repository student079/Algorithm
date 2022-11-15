cnt = 0
proc = []


def hanoi(num, bef, mid, aft):
    global cnt
    global proc
    if num == 1:
        proc.append([bef, aft])
        cnt += 1
    else:
        hanoi(num-1, bef, aft, mid)
        proc.append([bef, aft])
        cnt += 1
        hanoi(num-1, mid, bef, aft)


num = int(input())
hanoi(num, "1", "2", "3")
print(cnt)
for i in proc:
    print(" ".join(i))
