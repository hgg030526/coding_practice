def solution(n):
    i = 1
    a = 1
    while True:
        if a > n:
            break   
        i += 1
        a *= i
    return i-1
