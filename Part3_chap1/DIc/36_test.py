# 점수가 60점 미만이면 'F(재시험)'으로 값을 변경하는 코드를 key()를 이용해서 만들어보자
scores = {'국어': 88, '영어': 55, '수학': 85, '과학': 57, '국사': 82}
print(f'scores : {scores}')

st = 60
F_dic = {}

for sub in scores.keys():
    if scores[sub] < st:
        scores[sub] = 'F(재시험)'
        F_dic[sub] ='F(재시험)'

print(f'scores : {scores}')
print(f'F_dic : {F_dic}')