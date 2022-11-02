num = int(input())

i = 665
cnt = 0

while num != cnt:
    i += 1
    idx = len(str(i))
    for k in range(idx-2):
        if str(i)[k] == "6" and str(i)[k+1] == "6" and str(i)[k+2] == "6":
            cnt += 1
            break

print(i)
