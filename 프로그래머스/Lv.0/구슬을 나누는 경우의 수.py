def solution(balls, share):
    answer = 1
    mod = 1
    for i in range(share, 0, -1):
        answer *= balls
        mod *= i
        balls -= 1

    return answer//mod


#다른 풀이 : comb() 함수 사용
import math

def solution(balls, share):
    return math.comb(balls, share)
