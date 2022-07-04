# 1부터 10까지의 정수가 중복되지 않고 섞여 있을 때 행운의 숫자 7의 위치를 찾자!

import random

sam_list = random.sample(range(1, 11), 10)
idx = sam_list.index(7)
ip = int(input('숫자 7의 위치 입력 : '))

if ip == idx:
    print('빙고!')
else:
    print('ㅜㅜ')

print(f'sam_list : {sam_list}')
print(f'idx : {idx}')
