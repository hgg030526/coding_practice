def solution(array):
    answer = sorted(array)[len(array)//2]
    return answer


#sorted(배열1) : 배열1은 바뀌지 않음 따라서 배열2 = sorted(배열1) 이런 식으로 사용 ---배열을 수정하고 싶지 않을 때
#sort() : 배열1.sort() 이런 식으로 사용 --- 배열을 수정해도 될 때 간단하게 사용 가능
#sorted(배열) 자체가 배열,  배열.sort()은 배열이 아님
