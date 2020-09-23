def solution(board):
    answer = 0
    N = len(board)
    direction = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    
    def bfs(cur_dir):
        nonlocal N, direction, answer
        queue = [(0, 0, 0, cur_dir)]
        check = [[0 for _ in range(N)] for _ in range(N)]
        check[0][0] = 1
        
        while queue:
            x, y, cost, cur_dir = queue.pop(0)
            if x == N-1 and y == N-1:
                answer.append(cost)
                continue
            for next_dir, (i, j) in direction.items():
                next_x, next_y = x + i, y + j
                if (cur_dir in ['L', 'R'] and next_dir in ['L', 'R']) or \
                   (cur_dir in ['U', 'D'] and next_dir in ['U', 'D']):
                    next_cost = cost + 100
                else:
                    next_cost = cost + 500
                    
                if (0 < next_x < N) and (0 < next_y < N) and \
                   (not board[next_y][next_x]) and \
                   (not check[next_y][next_x]) or (check[next_y][next_x] < next_cost):
                    check[next_y][next_x] = next_cost
                    queue.append((next_x, next_y, next_cost, next_dir))
    
    bfs('R')
    print(answer)
    
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))