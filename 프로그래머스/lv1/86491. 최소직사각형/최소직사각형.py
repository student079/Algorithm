def solution(sizes):
    a = 0
    b = 0
    for size in sizes:
        if b < min(size):
            b = min(size)
        if a < max(size):
            a = max(size)
    return a*b