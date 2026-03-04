def solution(babbling):
    answer = 0
    for b in babbling:
        arr = [b]
        for w in ['aya', 'ye', 'woo', 'ma']:
            t = []
            for a in arr:
                t += a.split(w)
            arr = t
        if len(''.join(arr)) == 0:
            answer += 1
            
    return answer


# 다른 풀이 : replace() 사용
def solution(babbling):
    answer = 0
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            b = b.replace(w,' ')
        if b.replace(' ','') == '':
            answer += 1
    return answer
