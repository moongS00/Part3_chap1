# 1. 사용자가 점수를 입력하면 과락 과목과 점수를 출력하는 프로그램
'''
minScore = 60
kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))
sci = int(input('과학 점수 : '))
his = int(input('국사 점수 : '))

scores = [['국어', kor],
          ['영어', eng],
          ['수학', mat],
          ['과학', sci],
          ['국사', his]]

for item in scores:
    if item[1] < minScore:
        print('과락 과목 : {}, 점수 : {}'.format(item[0], item[1]))
'''

# 2. 학급 학생 수가 가장 작은 학급과 가장 많은 학급 출력
st = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

minC = st[0]
maxC = st[0]

for Class, cnt in st:
    if cnt < minC[1]:
        minC = [Class, cnt]

    elif cnt > maxC[1]:
        maxC = [Class, cnt]

print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minC[0], minC[1]))
print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxC[0], maxC[1]))
