# while과 if문을 사용한 과락 과문 출력

stand = 60

scores = (('국어', 58), ('영어', 77), ('수학', 89), ('과학', 99), ('국사', 50))

n = 0
while n < len(scores):
    if scores[n][1] < stand:
        print('과락 과목 : {}, 점수 : {}'.format(scores[n][0], scores[n][1]))

    n += 1