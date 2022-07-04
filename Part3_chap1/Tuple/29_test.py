# 1. 사용자가 점수를 입력하면 과락 과목과 점수를 출력
'''
stand = 60

kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
mat = int(input('수학 점수 입력 : '))
sci = int(input('과학 점수 입력 : '))
his = int(input('국사 점수 입력 : '))

scores = (('국어', kor), ('영어', eng), ('수학', mat), ('과학', sci), ('국사', his))

for item in scores:
    if item[1] < stand:
        print('과락 과목 : {}, 점수 : {}'.format(item[0], item[1]))

'''


# 2. 학생 수가 가장 많은 학급과 적은 학급 출력
st = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

mins = st[0][1]
mins_i = st[0][0]
mxas = 0
mxas_i = 0

for idx, val in st:
    if val < mins:
        mins = val
        mins_i = idx

    if idx == 0 or val > mxas:
        mxas = val
        mxas_i = idx

print('학생 수가 가장 적은 학급(학생수) : {}학급({}명)'.format(mins_i, mins))
print('학생 수가 가장 많은 학급(학생수) : {}학급({}명)'.format(mxas_i, mxas))