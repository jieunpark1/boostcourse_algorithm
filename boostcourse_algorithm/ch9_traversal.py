#순회: 체계적으로 그래프의 모든 노드를 방문. 각 노드는 최소 한 번 이상 방문.divmod
# - 목적: 그래프 구조 탐색, 특정 조건 만족 정점 찾기
# - 장점: 그래프의 구조를 이해, 문제 해결 기반
# - 예시: 최단 경로 탐색, 사이클 검출, 위상 정렬 등의 그래프 알고리즘을 효과적으로 적용 (DFS, BFS)

#순회=탐색 이라고 생각하고 강의 듣기

#BFS(Breadth)
## 외우기!!
#변수: graph, start_v, q, visited=[]
from collections import deque

def bfs(graph, start_v):
    # 시작점 설정
    q = deque()
    q.append(start_v)

    # 시작점 방문 도장
    visited = {start_v:True}

    while q:
        #방문
        cur_v = q.popleft()

        #다음 방문 '예약' + '방문' 도장 찍기
        for next_v in graph[cur_v]: #인접 리스트, graph[cur_v]=>연결된 노드
            if next_v not in visited:  #방문 하지 않았을 때에만 예약한다.
                q.append(next_v)  #예약
                visited[next_v] = True #방문 도장

graph = {
  0: [1, 3, 6],
  1: [0, 3],
  2: [3],
  3: [0, 1, 2, 7],
  4: [5],
  5: [4, 6, 7],
  6: [0, 5],
  7: [3, 5]
}
 # 위의 인접 리스트를 시각화된 그래프를 머릿속으로 떠올리기
start_v = 0
res = bfs(graph, start_v=0)
print(res)