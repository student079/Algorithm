def solution(s):
    
    # 문자 나오면 그때부터 문자열로 길이 비교하고, 내용비교해서 딕셔너리에 키가 있는지 확인
    # 없으면 한칸 더 해서 맞을 때까지 늘림
    # 맞으면 그거 결과문자열에 붙임
    # 숫자면 그냥 붙임
    
    answer = ""
    int_a = ord('a')
    int_z = ord('z')
    convert = dict({'one': '1',
                   'two': '2',
                   'three': '3',
                   'four': '4',
                   'five': '5',
                   'six': '6',
                   'seven': '7',
                   'eight': '8',
                   'nine': '9',
                   'zero': '0'})
    convert_keys = list(convert.keys())

    str = ""
    for c in s:
        if int_a <= ord(c) <= int_z:
            str+=c
            if str in convert_keys:
                answer+=convert[str]
                str=""
        else:
            answer+=c
            str=""
    
    return int(answer)