# 1. 가장 좋아하는 스포츠가 몇번째에 있는지 출력

sports = ['농구', '수구', '축구', '마라톤', '테니스']
favS = input('가장 좋아하는 스포츠 입력: ')

favIdx = 0
for idx, val in enumerate(sports):
    if val == favS:
        favIdx = idx +1

print('{}(은)는 {}번째에 있습니다.'.format(favS, favIdx))


# 2. 사용자가 입력한 문자열에서 공백의 개수 출력

mess = input('메시지 입력 : ')
cnt = 0

for idx, val in enumerate(mess):
    if val == '':
        cnt += 1

print('공백 개수 : {}'.format(cnt))