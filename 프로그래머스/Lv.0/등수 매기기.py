# 실패한 코드 : .index()를 사용하면 안됨. 같은 원소일 경우 동일한 인덱스를 불러오기 때문
def solution(score):
    ranks = [0]*len(score)
    sorted_s = sorted(score,key=lambda x:-(x[0]+x[1]))
    avg,rank,i = sum(sorted_s[0]),1,0
    
    while i < len(score):
        while avg == sum(sorted_s[i]):
            ranks[score.index(sorted_s[i])] = rank
            i += 1
            if i == len(score):
                break
        if i == len(score):
                break
        avg = sum(sorted_s[i])
        rank = i+1
        ranks[score.index(sorted_s[i])] = rank
        i += 1
    
    return ranks

# 다른 풀이(by GPT) : 처음 정렬을 할 때 인덱스를 포함한 튜플로 정렬
def solution(score):
    total_score = [(sum(s),i) for i,s in enumerate(score)]
    total_score.sort(reverse = True)
    
    ranks = [0]*len(score)
    pre_total = -1
    rank = 1
    
    for i,(total,index) in enumerate(total_score):
        if total != pre_total:
            rank = i+1
        
        ranks[index] = rank
        pre_total = total
    
    return ranks

# 다른 풀이 : index()에서 같은 값일 때 가장 앞의 인덱스를 도출하는 점을 활용
def solution(score):
    a = sorted([sum(s) for s in score],reverse = True)
    
    return [a.index(sum(s))+1 for s in score]
