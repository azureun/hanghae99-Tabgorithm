from collections import deque

def bfs(n, m, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 상하좌우 이동
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]  # 3차원 방문 배열
    queue = deque([(0, 0, 0, 1)])  # (x, y, 벽 부숨 여부, 거리)
    visited[0][0][0] = True

    while queue:
        x, y, wall_broken, dist = queue.popleft()

        # (N, M)에 도달한 경우
        if x == n - 1 and y == m - 1:   # 시작점(0,0)에서 끝점(n-1, m-1)로 이동하는 최소거리 탐색
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:  # 유효한 범위인지 확인
                # 벽을 만나지 않은 경우 > 이동하는 곳이 벽이아닌 위치(0) & 해당 상태에서 방문하지 않으면 큐에 추가
                if grid[nx][ny] == 0 and not visited[nx][ny][wall_broken]: # 현재 벽을 부쉈는지 여부(wall_broken)를 기준으로 방문 여부 확인
                    visited[nx][ny][wall_broken] = True
                    queue.append((nx, ny, wall_broken, dist + 1))
                # 벽을 만났지만 아직 부술 수 있는 경우
                elif grid[nx][ny] == 1 and wall_broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1  # 목표 지점에 도달할 수 없는 경우

n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
print(bfs(n, m, grid))
