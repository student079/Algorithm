import sys

M = int(sys.stdin.readline())

s = set()

def add(x):
    s.add(x)

def remove(x):
    if x in s:
        s.remove(x)

def check(x):
    if x in s:
        print("1")
    else:
        print("0")

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    s.update(range(1, 21))

def empty():
    s.clear()

commands = {
    "add": add,
    "remove": remove,
    "check": check,
    "toggle": toggle,
    "all": all,
    "empty": empty
}

for _ in range(M):
    command = sys.stdin.readline().rstrip('\n')
    if command == "all":
        all()
    elif command == "empty":
        empty()
    else:
        cmd, arg = command.split()
        commands[cmd](int(arg))
