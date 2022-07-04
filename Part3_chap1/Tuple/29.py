# 반복문과 조건문을 사용해 과락 과목 출력하기

stand = 60

scores = (('국어', 58), ('영어', 77), ('수학', 89), ('과학', 99), ('국사', 50))

for idx, val in scores:
    if val < stand:
        print('과락 과목 : {}, 점수 : {}'.format(idx, val))

for item in scores:
    if item[1] < stand:
        print('과락 과목 : {}, 점수 : {}'.format(item[0], item[1]))