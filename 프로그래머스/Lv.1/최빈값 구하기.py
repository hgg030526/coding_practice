def solution(array):
    list = [0 for x in range(1000)]  #[0]*1000   #list 대신 cnt, lst 사용하기
    for num in array:
        list[num] = list[num] + 1
    
    if list.count(max(list)) > 1:
        answer = -1
    else:
        answer = list.index(max(list))
    
    return answer




#다른 풀이 : [1 2 2 3 3 3] -> [2 3 3] -> [3]
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
