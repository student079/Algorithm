import sys

st1 = list(sys.stdin.readline().rstrip('\n'))
st2 = []

for _ in range(int(sys.stdin.readline())):
	command = sys.stdin.readline().rstrip('\n')
	com = command[0]
	
    #커서를 기준으로 왼쪽은 st1, st2로 나누기
	if com == 'L':
		if st1:
			st2.append(st1.pop())
	elif com == 'D':
		if st2:
			st1.append(st2.pop())
	elif com == 'B':
	    if st1:
		    st1.pop()
	else:
		st1.append(command[2])
	
#오른쪽 st2를 뒤집어서 붙이기
st1.extend(reversed(st2))
print(''.join(st1))