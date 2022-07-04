# 하루동안 헌혈을 진행한 후 혈액형 별 개수를 파악하는 프로그램

import random
types = ['A', 'B', 'AB', 'O']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print(f'todayData : {todayData}')
print(f'todayData elngth : {len(todayData)}')

for type in types:
    print('{}형\t : {}개'.format(type, todayData.count(type)))