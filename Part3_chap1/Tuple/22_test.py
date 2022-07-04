# 컴퓨터가 1부터 10까지 5개의 난수를 생성한 후, 사용자가 입력한 숫자가 있는지 출력

import random

ran_num = random.sample(range(1, 11), 5)

u_num = int(input('숫자 입력(확률 50%) : '))

if u_num in ran_num:
    print('빙고!')
else:
    print('다음 기회에~')

print(f'ran_num : {ran_num}')
print(f'u_num : {u_num}')