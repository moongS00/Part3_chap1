# 최저, 최고값 삭제하기

playScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print(f'playScore : {playScore}')
minScore = 0
minScoreIdx = 0
maxScore = 0
maxScoreIdx = 0

for idx, score in enumerate(playScore):
    if idx == 0 or score < minScore:
        minScore = score
        minScoreIdx = idx

    if score > maxScore:
        maxScore = score
        maxScoreIdx = idx

print(f'minScore : {minScore}, minScoreIdx : {minScoreIdx}')
playScore.pop(minScoreIdx)
print(f'playScore : {playScore}')
print(f'maxScore : {maxScore}, maxScoreIdx : {maxScoreIdx}')
playScore.pop(maxScoreIdx)
print(f'playScore : {playScore}')
