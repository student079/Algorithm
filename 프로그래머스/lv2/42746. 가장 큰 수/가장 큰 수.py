def solution(numbers):
    
    # 제일 앞자리 큰순으로 정렬해서 붙이기
    
    # 문자열로 바꾸고 1000이하니까 세자리만 비교하면 돼
    # 람다식 사용
    numbers = list(map(str,numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse = True) #세자리만 비교해서 정렬
    
    # 000붙어나오는거 방지
    numbers = str(int("".join(numbers)))
    
    return numbers