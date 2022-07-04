# 5명의 학생 이름을 리스트에 저장하고 인덱스가 홀수인 하갱과 짝수(0포함)인 학생을 구분해서 인덱스와 학생 이름을 출력해보자

st = ['김성예', '신경도', '박기준', '최승철', '황동석']

print('-----인덱스가 짝수인 학생-----')
print('st[0] : {}'.format(st[0]))
print('st[2] : {}'.format(st[2]))
print('st[4] : {}'.format(st[4]))
print('-----인덱스가 홀수인 학생-----')
print('st[1] : {}'.format(st[1]))
print('st[3] : {}'.format(st[3]))

for i in range(5):
    if i % 2 == 0:
        print('인덱스 짝수 : st[{}] : {}'.format(i, st[i]))
    else:
        print('인덱스 홀수 : st[{}] : {}'.format(i, st[i]))