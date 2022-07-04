# for문과 if문을 사용한 리스트 조회

minScore = 60
scores = [['국어', 58],
          ['영어', 77],
          ['수학', 89],
          ['과학', 99],
          ['국사', 50]]

for item in scores:
    if item[1] < minScore:
        print('과락 과목 : {}, 점수 : {}'.format(item[0], item[1]))

for sub, score in scores:
    if score >= minScore: continue
    print('과락 과목 : {}, 점수 : {}'.format(sub, score))