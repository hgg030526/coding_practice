# 2차원 배열 생성
b = [[0]*(n+2)]*(n+2)
# 이런 식으로 생성하게 되면 각 행의 주소값이 동일하게 생성됨 b[1][1] 값 하나를 수정하려 해도 b[_][1] 모든 값이 다 수정됨
b = [[0]*(n+2) for _ in range(n+2)]
# 위와 같이 생성해야 각 행이 독립적으로 생성됨

def solution(board):
    ans = 0
    n = len(board[0])
    b = [[0]*(n+2) for _ in range(n+2)]
    
    #(n+2)*(n+2) 짜리 배열에 board 배열 넣기
    for i in range(1,n+1):
        b[i][1:n+1] = board[i-1]
    
    #주변에 1이 없을 경우 ans에 1 추가
    for i in range(1,n+1):
        for j in range(1,n+1):
            one_n = sum(sum(b[k][j-1:j+2]) for k in range(i-1,i+2))
            ans += 1 if one_n == 0 else 0
    return ans


# 다른 풀이 : 위험한 좌표를 set()에 저장해 놓은 후 보드 범위 내의 위험한 좌표 수를 활용해 정답 구하기
# set.add() : 한 번에 원소 하나만 넣을 수 있음, set.update() : 한 번에 원소 여러개 넣을 수 있음
def solution(board):
    n = len(board[0])
    danger = set()
    
    for i,row in enumerate(board):
        for j,x in enumerate(row):
            if x == 0:
                continue
            danger.update((i+di,j+dj) for di in [-1,0,1] for dj in [-1,0,1])
            
    return n*n - sum(0 <= i < n and 0 <= j < n for i,j in danger)  # generator expression 
  
