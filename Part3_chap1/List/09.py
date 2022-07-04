# enumerate() 함수

sports = ['농구', '수구', '축구', '마라톤', '테니스']

for idx, value in enumerate(sports):
    print('{} : {}'.format(idx, value))


# 문자열에도 적용 가능
str = 'Hello Python.'
for idx, value in enumerate(str):
    print('{} : {}'.format(idx, value))