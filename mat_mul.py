# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-12-02
# 과제번호: 12주차 1번

import time
import numpy as np
import matplotlib.pyplot as plt

def mat_mul(arr1, arr2):
    if len(arr1) == len(arr2):
        answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
        for i in range(len(arr1)):
            for j in range(len(arr2[0])):
                for k in range(len(arr1[0])):
                    answer[i][j] += (arr1[i][k] * arr2[k][j])
        return answer
    else:
        raise ValueError
  
m10 = np.random.randn(10, 10)
m50 = np.random.randn(50, 50)
m100 = np.random.randn(100, 100)
m200 = np.random.randn(200, 200)
m300 = np.random.randn(300, 300)
matrix = (m10, m50, m100, m200, m300)

timesmy = []
timesnp = []
for l in range(5):
    t = time.time()
    mat_mul(matrix[l], matrix[l])
    ends = time.time() - t
    timesmy.append(ends)

for m in range(5):
    t = time.time()
    np.dot(matrix[m], matrix[m])
    ends = time.time() - t
    timesnp.append(ends)

plt.plot(timesmy)
plt.plot(timesnp)
plt.xlabel('Matrix size')
plt.ylabel('Elapsed Time(s)')
plt.legend(['mat_mul', 'np.dot()'])
plt.show()