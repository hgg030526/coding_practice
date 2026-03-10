#최소공배수 & 최대공약수 구하기
def solution(n):
    for x in range(n*6, 1, -1):
        if n%x == 0 and 6%x==0:
            return (n*6//x) // 6
    
    return n
