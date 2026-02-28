def solution(dots):
    a = [[0,1,2,3],[0,2,1,3],[0,3,1,2]]
    
    for i in range(3):
        slope1 = (dots[a[i][0]][1]-dots[a[i][1]][1])/(dots[a[i][0]][0]-dots[a[i][1]][0])
        slope2 = (dots[a[i][2]][1]-dots[a[i][3]][1])/(dots[a[i][2]][0]-dots[a[i][3]][0])
        if slope1 == slope2:
            return 1
    return 0


# 다른 풀이 : 일일이 다 계산
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0
