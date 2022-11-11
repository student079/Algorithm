import sys

item = int(sys.stdin.readline())

people = []

for _ in range(item):
    age, name = sys.stdin.readline().strip("\n").split()
    people.append((int(age), name))

people.sort(key=lambda x: (x[0]))

for i in people:
    print("{} {}".format(i[0], i[1]))
