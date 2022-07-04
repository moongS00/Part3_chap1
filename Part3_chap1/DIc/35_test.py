# 1. 학생의 시험점수가 60점 미만이면 F(재시험)으로 값 변경하기
'''
scores = {'국어': 88, '영어': 55, '수학': 85, '과학': 57, '국사': 82}
print(f'scores : {scores}')

st = 60

for i in scores:
    if scores[i] < st:
        scores[i] = 'F(재시험)'


print(f'scores : {scores}')
'''

# 2. 하루에 몸무게(kg)와 신장(m)이 각각 -0.3kg, +0.001m씩 변한다고 할 때, 30일 후의 몸무게와 신장의 값을 저장하고 BMI값을 출력하자
bi = {'이릅': '홍길동', '몸무게': 83.0, '신장': 1.8}
bmi = bi['몸무게'] / (bi['신장'] ** 2)

print(f'bi : {bi}')
print('bmi : %.2f' %bmi)
n = 1
while n <= 30:
    bi['몸무게'] -= 0.3
    bi['신장'] += 0.001
    n += 1

bi['몸무게'] = round(bi['몸무게'], 1)
bi['신장'] = round(bi['신장'], 2)

print()
print(f'bi : {bi}')
print('bmi : %.2f' %bmi)
