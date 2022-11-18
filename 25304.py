price_all = int(input())
item = int(input())

i = 0
price_temp = 0
while i < item:
    price, many = map(int, input().split())
    price_temp += price*many
    i += 1

if price_all == price_temp:
    print("Yes")
else:
    print("No")
