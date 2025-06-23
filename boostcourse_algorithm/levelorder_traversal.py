# *** 외우기 ***

from collections import deque

#queue 자료구조 이용

def levelOrder(root):
  #필요변수
  visited = []
  
  #root 정의 (base case)
  if root is None:
    return 0         #base case 정의 전, root 없을 시 오류나는 부분 해결
    
  q = deque()
  q.append(root)     #base case 지정. root가 가장 먼저 queue에 들어가도록 한다.
  

  #X(current_node)를 queue에서 popleft, 동시에, (  visited에 X 추가 | X의 left/right children queue에 넣음 ) -> q에 모든 노드가 순환되어서 남아있는게 없을 때까지 진행
  while q:
    x = q.popleft() #x가 자동으로 큐의 front로 이동함
  
    visited.append(x) #visited
    
    if x.left: q.append(x.left)
    if x.right: q.append(x.right)
    
  return visited

root = 3
res = levelOrder(root)
print(res)
