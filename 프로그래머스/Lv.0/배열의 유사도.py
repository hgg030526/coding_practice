def solution(s1, s2):
    return sum([1 for w in s2 if w in s1])

#교집합 활용
def solution(s1, s2):
    return len(set(s1)&set(s2));
