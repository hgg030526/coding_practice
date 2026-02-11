def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        lst = []
        for j in range(i,i+n):
            lst.append(num_list[j])
        answer.append(lst)
    return answer


#다른 풀이 : slicing 사용
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
