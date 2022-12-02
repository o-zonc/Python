# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-10-14
# 과제번호: 7주차 1번

from listfunc import *

scorelist = [i for i in range(1,11)]

scorelist = list_reverse(scorelist)
print(f'Reverse : {scorelist}')

scorelist = list_shuffle(scorelist)
print(f'Shuffle : {scorelist}')

scorelist = list_filter(scorelist, 6)
print(f'Filter : {scorelist}')

scorelist = list_clear(scorelist)
print(f'Clear : {scorelist}')