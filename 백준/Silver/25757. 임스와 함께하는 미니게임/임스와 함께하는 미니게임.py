# N <= 100000 십만
# Y 2, F 3, O 4
import sys

N, gameType = sys.stdin.readline().rstrip().split()

gameNeedPeople = dict({'Y': 1, 'F' : 2, 'O': 3})

people = set()
for _ in range(int(N)):
    people.add(sys.stdin.readline().rstrip())

print(len(people)//gameNeedPeople[gameType])