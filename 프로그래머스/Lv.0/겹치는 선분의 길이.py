# 내 풀이 : 배열에 선분이 있는 칸을 저장 -> 2 이상이면 선분이 겹친거임
def solution(lines):
    answer = 0
    start = min(l[0] for l in lines)
    end = max(l[1] for l in lines)
    arr = [0]*(end-start)
    lines = [[lines[i][0]-start,lines[i][1]-start] for i in range(3)]
        
    for l in lines:
        for i in range(l[0],l[1]):
            arr[i] += 1
    return sum(a > 1 for a in arr)


# 다른 풀이 : set 교집합 사용하기
def solution(lines):
    sets = [set(range(min(l),max(l))) for l in lines]
    return len((sets[0]&sets[1]) | (sets[1]&sets[2]) | (sets[0]&sets[2]))
