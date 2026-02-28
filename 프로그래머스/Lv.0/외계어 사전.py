def solution(spell, dic):
    for w in dic:
        if len(spell) == sum(s in w for s in spell):
            if len(spell) == sum(w.count(s) for s in spell):
                return 1
    return 2


# 다른 풀이 : sorted(문자열) = 각 알파벳별로 정렬된 배열
def solution(spell, dic):
    for d in dic:
        if sorted(spell) == sorted(d):
            return 1
    return 2
