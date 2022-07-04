# 학급별 학생 수, 전체 학생 수, 평균 학생 수 출력

st = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

sum = 0

for idx, val in st:
    print('{}학급 학생 수 : {}명'.format(idx, val))
    sum += val
    
avg = sum / len(st)
print(f'전체 학생 수 : {sum}명')
print(f'평균 학생 수 : {avg}명')