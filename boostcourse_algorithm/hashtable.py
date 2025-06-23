#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys


#hash table = 딕셔너리
#direct address table: key-value 쌍
# - 단점: 엄청 큰 arr 선언 필 / 많은 양의 메모리를 낭비 / key 문자열인 경우, 인덱스 저장 불가
#따라서, hash table 사용: hashfunction 사용
# HashFuntion: hash function이 정한 범위 내에서 key를 넣으면 index(주소)를 지정하여 그곳에서
# key-value를 저장
# - 장점: 큰 arr 선언 안해도됨 / key값이 문자열인 경우도 인덱스 저장 가능
# - 단점: collision 발생. : hashfunction의 return값이 같아서 index가 겹치면 충돌 발생
# -- 해결: 0번에서 충돌 -> 1번에 저장, 1번에서 충돌 -> 2번에 저장
# 따라서, hashfunction의 return값이 고르게 퍼지도록 함수를 잘 작성해주어야 함.
# 파이썬에서는 hashfunction을 통해 dictionary로 구현되어있음.
# 내부 동작들을 알면 시간복잡도를 생각할 수 있다. (디테일하게는 기억 안해두됨)


#딕셔너리 value값 탐색 O(n)
#딕셔너리 key값 탐색 O(1) 
## - 왜? 특정 key를 hash function에 넣어서 return값을 따라 가서 그 값이 아니면 존재하지 않는 것이라서!
## <- 개싱기.. 역시 내부 동작을 알아야하는 이유..,


dic_ = {}
dic_[20250622] = "박지은"
dic_[20250628] = "김지은"
print(dic_)

print(dic_.items())
# for k, v in dic_.items():
#     print(k, v)
#     if v == "박지은":
#         print("찾았다!")   #O(n)

for "20250622" in dic_: #hash function  in dictionary => O(1) #리스트의 경우 O(n)
    print("찾았다!")
else:
    print("없다")