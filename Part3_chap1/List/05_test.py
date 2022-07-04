# 학급별 학생수, 전체 학생수, 평균 학생 수 구하기

st = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

sum = 0

for classNo, cnt in st:
    print('{}학급 학생 수 : {}명'.format(classNo, cnt))
    sum += cnt

print(f'총 학생 수 : {sum}명')
print(f'평균 학생 수 : {sum / len(st)}명')
