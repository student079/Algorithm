import sys

# input
N = int(sys.stdin.readline())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip('\n'))

# 단어 하나씩 뒤 문자부터 보면서 자리수 딕셔너리에 추가
# 딕셔너리에 이미 있는 문자면 있던거에 + 자리수
d = dict()
for word in words:
    i = 1
    word = list(word)
    while word:
        alpha = word.pop()
        if alpha in d:
            d[alpha] += i
        else:
            d[alpha] = i
        i *= 10

# 단어들의 자리수들을 내림차순 정렬해주고
# 큰거부터 9,8,7,6,...,1 곱해서 더해주기
nums = list(d.values())
nums.sort(reverse=True)
answer = 0
digit = 9
for num in nums:
    answer += digit*num
    digit -= 1

print(answer)