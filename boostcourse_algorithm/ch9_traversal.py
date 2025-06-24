#순회: 체계적으로 그래프의 모든 노드를 방문. 각 노드는 최소 한 번 이상 방문.divmod
# - 목적: 그래프 구조 탐색, 특정 조건 만족 정점 찾기
# - 장점: 그래프의 구조를 이해, 문제 해결 기반
# - 예시: 최단 경로 탐색, 사이클 검출, 위상 정렬 등의 그래프 알고리즘을 효과적으로 적용 (DFS, BFS)

#순회=탐색 이라고 생각하고 강의 듣기

#BFS(Breadth)
## 외우기!!
#변수: graph, start_v, q, visited=[]
#***여러가지로 "확장"해보는 게 좋음***
#리스트 사용하는 경우도 꽤 많으니, 리스트 & 딕셔너리 둘다 잘 알아두기!

from collections import deque

def bfs(graph, start_v):
    # 시작점 설정
    q = deque()
    q.append(start_v)

    # 시작점 방문 도장
    #visited = {start_v:True}   #딕셔너리 생성과 동시에 삽입
    #visited = {} / visited[start_v] = True
    visited = [False] * 8 #리스트로 쓰려면 개수대로 초기 세팅을 해주어야 함
    print(visited)
    visited[start_v] = True

    while q:
        #방문
        print(q)
        cur_v = q.popleft()
        print(cur_v)
        if cur_v == 5: print("5번 노드 찾았다!")

        #다음 방문 '예약' + '방문 도장' 찍기
        for next_v in graph[cur_v]: #인접 리스트, graph[cur_v]=>연결된 노드
            if not visited[next_v]:  # -- list
            #if next_v not in visited:  #방문 하지 않았을 때에만 예약한다. -- dict
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
bfs(graph, start_v=0)


#DFS (Depth-First Search)
# - 특징: 깊이 들어갔다가 빠져나올 곳을 알아야 하므로, Stack 혹은 재귀 자료구조를 사용
# - 구동 방식: next_v를 방문 안했으면 dfs 재귀적 실행 
# - 구동 방식 명확하게 이해하고 있어야 함! (챕터9, DFS 코드 설계와 구현)

def defs(graph, cur_v):
    #a. 방문: 1. 스택에 넣기 2. 방문도장 찍기
    #b. cur_v와 연결된 노드 찾기: 1. 연결된 노드 for loop 2. 방문 도장 찍혔는지 확인
    #c. next_v 방문 안했으면: 1. 해당 vertex에 대해 재귀적 함수 dfs(next_v) 모두 실행 1. 방문 도장 찍기

    #a.
    visited[cur_v] = True

    #b.
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            #1. 재귀적
            dfs(next_v)

            # stack.append(next_v)
            # visited[next_v] = True
