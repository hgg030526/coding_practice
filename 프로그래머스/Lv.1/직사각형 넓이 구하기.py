def solution(dots):
    l,h = [],[]
    dots *= 2
    for i in range(4):
        l.append(dots[i][0]-dots[i+1][0])
        h.append(dots[i][1]-dots[i+1][1])

    return max(l)*max(h)

#다른 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
