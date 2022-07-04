# 최저, 최고 점수 삭제 후 총점과 평균 출력

playScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print(f'playScore : {playScore}')

playScore.sort()
print(f'playScore : {playScore}')
playScore.pop()
playScore.pop(0)
print(f'playScore : {playScore}')

sum = 0
for sco in playScore:
    sum += sco

avg = sum / len(playScore)

print('총점 : %.2f' %sum)
print('평균 : %.2f' %avg)
