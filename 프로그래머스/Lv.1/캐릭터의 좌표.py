def solution(keyinput, board):
    answer = [0,0]
    for d in keyinput:
        if d == 'up':
            if answer[1] == board[1]//2:
                continue
            else:
                answer[1] += 1
        elif d == 'down':
            if answer[1] == -(board[1]//2):  #괄호 필수
                print(0)
                continue
            else:
                answer[1] -= 1
        elif d == 'left':
            if answer[0] == -(board[0]//2):
                continue
            else:
                answer[0] -= 1
        else:
            if answer[0] == board[0]//2:
                continue
            else:
                answer[0] += 1
    return answer


#다른 풀이 : min,max 사용
def solution(keyinput, board):
    p = [0,0]
    for d in keyinput:
        if d == 'up':
            p[1] = min(board[1]//2, p[1] + 1)
        elif d == 'down':
            p[1] = max(-(board[1]//2), p[1] - 1)
        elif d == 'left':
            p[0] = max(-(board[0]//2), p[0] - 1)
        else:
            p[0] = min(board[0]//2, p[0] + 1)
    return p
