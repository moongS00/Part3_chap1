# 학급별 학생수, 전체 학생 수, 평균 학생 수 출력
st = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

n = 0
sum = 0
avg = 0

while n < len(st):
    print('{}학급 학생 수 : {}'.format(st[n][0], st[n][1]))
    sum += st[n][1]
    n += 1

avg = sum / len(st)
print('전체 학생 수 : {}'.format(sum))
print('평균 학생 수 : {}'.format(avg))