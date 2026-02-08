def solution(num_list):
    even = sum([1 for x in num_list if x%2 == 0])
    odd = sum([1 for x in num_list if x%2 == 1])
    return [even, odd]

#다른풀이
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2] += 1
    return answer
