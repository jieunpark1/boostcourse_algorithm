#백트랙킹: 완전 탐색에서 좀 더 발전된 개념
#: 완전탐색 하는 와중에 
# solution이 될 가능성이 없는 candidate은 더 이상 탐색하지 않고 candidate를 포기(batrack)하면서 탐색하는 방법

#문1) word search; 가로 또는 세로로 이어서 "cat"이라는 글자를 만들어주세요.
##  E  B  N
##  T  Z  L
##  A  C  D

## 트리를 그려본다.

## E     B      N      T      Z      L ..  C         
## |     |      |      |      |      |     |
#  x     x      x       x     x      x     o
#                                          A
#                                          |
#                                          o
#                                          T




#문2) 핸드폰 키패드에서 '4 5 6 ' 순서대로 입력해서 'kor'을 작성할 수 있나요?
#4 -> j k l
#5 -> m n o
#6 -> p q r
# tree 그리기
# j      k        l
#m n o  m n o    m n o
# 
#   |     |        |
#  j탈락  k 오케이   l은 후보도 안됨   (backtrack)
#            r
#            |
#           kor 완성