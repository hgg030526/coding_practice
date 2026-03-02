def solution(A, B):
    for push in range(len(A)):
        if A == B:
            return push
        A = A[-1]+A[:-1]
        
    return -1
