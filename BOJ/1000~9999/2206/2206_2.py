import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().rstrip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0


def bfs():
    deq = deque()
    deq.append((0, 0))
    dist[0][0] = 1
    while deq:
        v = deq.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[v[0]][v[1]] + 1
                deq.append((nx, ny))
