def solution(n):
    return sum([1 for x in range(1, n+1) if n%x == 0])


#다른 풀이 : 시간복잡도가 반띵
def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2

            if i * i == n:
                answer -= 1

    return answer
