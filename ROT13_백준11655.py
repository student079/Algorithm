import sys

stri = sys.stdin.readline().rstrip('\n')

result = ""
for i in list(stri):
    if i.isalpha() and i.islower():
        temp = ord(i)+13
        if temp > 122:
            temp = temp - 122 + 96
    elif i.isalpha() and i.isupper():
        temp = ord(i)+13
        if temp > 90:
            temp = temp - 90 + 64
    else:
        temp = ord(i)

    result += chr(temp)

print(result)
