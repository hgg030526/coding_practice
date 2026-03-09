# 정확성 100, 효율성 0
def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    
    return participant[0]
