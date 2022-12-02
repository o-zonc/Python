# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-10-14
# 과제번호: 7주차 1번

import random

def list_reverse(scorelist):
    temp = []
    for i in range(len(scorelist)):
        temp.append(scorelist[-i - 1])
    for i in range(len(scorelist)):
        scorelist.pop()
    for i in temp:
        scorelist.append(i)

def list_filter(scorelist, n):
    temp = [i for i in scorelist if i < n]
    for i in range(len(scorelist)):
        scorelist.pop()
    for i in temp:
        scorelist.append(i)

def list_shuffle(scorelist):
    temp = []
    uniq = random.sample(range(len(scorelist)), len(scorelist))
    for i in range(len(scorelist)):
        a = uniq[i]
        temp.append(scorelist[a])
    for i in range(len(scorelist)):
        scorelist.pop()
    for i in temp:
        scorelist.append(i)

def list_clear(scorelist):
    for i in range(len(scorelist)):
        scorelist.pop()