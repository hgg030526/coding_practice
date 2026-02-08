def solution(dot):
    if dot[0]*dot[1] > 0:
        return 1 if dot[0] > 0 else 3
    else:
        return 2 if dot[0] < 0 else 4


#다른 풀이 : 참거짓 활용
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
