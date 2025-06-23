# DP(dynamic programming)
# 큰 문제를 작은 문제(subproblem)로 나누어 해결한 후, 그 결과를 저장하여 중복 계산을 줄이는 최적화기법
# ***-- 중복계산해야하는 하위문제가 있다(overlapping subproblem)
# -- 따라서, 한 번 계산한 결과는 메모리에 저장하여 재계산하지 않도록 한다. (memoiation, dp table)***
# -- 하위 문제에 대한 답을 통해 원래 문제에 대한 답을 계산한다 (optimal substructure 최적 부분 구조)
## 예) 피보나치 수열 10 -> 9 8 ... 3 -> 1 2 (쉬운 부분 문제로 나누어짐) 
# 하위 부분 문제에서 구한 답이 합쳐져 큰 문제의 최적의 답을 구할 수 있는 구조


# 피보나치 수열 base case -- sum of 1st and 2nd -> 3nd
# 문) 7번째 피보나치 수를 반환하라.

#완전 탐색 방식 (base case & recurrence correlation)
# 접근방법 => 완전탐색 (재귀)
#1. 크고 복잡한 문제를 하위 문제로 나눈다.
#2. 하위 문제에 대한 답을 계산한다.
#3. 하위문제에 대한 답으로 원래 답을 구한다.
#-- 문제: 중복된 계산이 너무많아 비효율적이다. => 중복 계산을 줄여보자

#DP 방식
# 접근 방법 
#2. 하위 문제에 대한 답을 계산한다.
# ㄴ 중복 하위문제 -- 예) f(3) 한번은 계산해야함. 이것을 hash table / list에 저장 -> 나중에 불러오면 됨
# ㄴ 계산 결과를 저장하여 중복된 문제에 사용
# 중복 계산이 필요한 시점에 memoization 했던 것을 가져다 그냥 쓰면 됨!
# -- 장점: O(2^n)에서 DP 사용 시, 총 O(2n) = O(n)으로 획기적으로 줄어버림.

#따라서,,.
# 재귀로 작성했는데 backtrack/중복된 문제가 있으면 DP를 사용하여 결과를 저장하면 효율성이 올라간다.



#재귀
def fibo_self(n):
    if n==1 or n==2:
        return 1
    return fibo_self(n-1) + fibo_self(n-2)

print(fibo_self(8))


#DP - 이제 있는 걸 갖다 써야하니까 memoization 할 공간을 만들어야 함 - 딕셔너리 n번째에 n번째 피보나치 수열값을 저장
#                                                            ㄴ 리스트보다 key값 찾는 시간복잡도 낮음(O(1))
# memo에 값이 없을 시에만 점화식 사용하고, memo에 값이 있으면 그 값을 끌어다 씀
# 근데 이걸 누군가는 계산해줘야하니, bottom-up 방식으로 진행될수밖에 없다.
print("============= DP - top-down ===============")
def fibo_dp(n):
    memo = {}
    if n==1 or n==2:
        return 1
    
    if n not in memo:   #아무도 안했으면 누군가는 해야지.. 직접 계산이 필요
        memo[n] = fibo_dp(n-1) + fibo_dp(n-2)
    print(memo)
    print("-----------------")
    return memo[n]  #누군가 계산해놓은 값을 가져다옴

print(fibo_dp(8))


print("============= DP - bottom-up ===============")

memo = {1:1, 2:1}

def fibo_dp_botup(n):

    if n==1 or n==2:
        return 1
    
    for i in range(3, n+1):   #아무도 안했으면 누군가는 해야지.. 직접 계산이 필요
        memo[i] = memo[i-1] + memo[i-2]
    print(memo)
    return memo[n]  #누군가 계산해놓은 값을 가져다옴

print(fibo_dp_botup(8))


def c_d(n):
    if n == 0:
        return "Done!"
    print(n)
    return c_d(n-1)
c_d(3)
