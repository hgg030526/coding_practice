def solution(array):
    list = [0 for x in range(1000)]  #[0]*1000   #list 대신 cnt, lst 사용하기
    for num in array:
        list[num] = list[num] + 1
    
    if list.count(max(list)) > 1:
        answer = -1
    else:
        answer = list.index(max(list))
    
    return answer
