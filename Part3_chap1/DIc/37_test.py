# 딕셔너리에 저장된 점수 중 최저 및 최고 점수를 삭제하기

scores = {'score1': 8.9, 'score2': 8.1, 'score3': 8.5, 'score4': 9.8, 'score5': 8.8}
print(f'scores : {scores}')
min_s = scores['score1']
min_k = ''
max_s = 0
max_k = ''

for key in scores.keys():
    if scores[key] < min_s:
        min_s = scores[key]
        min_k = key

    if max_s < scores[key]:
        max_s = scores[key]
        max_k = key


del scores[min_k]
del scores[max_k]
print(f'scores : {scores}')


