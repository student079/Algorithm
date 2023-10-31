T = int(input())

days = (0,31,28,31,30,31,30,31,31,30,31,30,31)

for t in range(1,T+1):
    d = input()
    year, month, day = d[:4], int(d[4:6]), int(d[6:])

    if 1<= month <= 12 and 1<= day <= days[month]:
        print(f'#{t} {year}/{str(month).zfill(2)}/{str(day).zfill(2)}')
    else:
        print(f'#{t} -1')




