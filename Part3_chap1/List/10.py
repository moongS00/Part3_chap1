# 리스트에 아이템 추가 : append()

st = ['김성예', '신경도', '박기준', '최승철', '황동석']
print('st : {}'.format(st))
print('st의 길이 : {}'.format(len(st)))
print('st의 마지막 인덱스 : {}'.format(len(st) - 1))

st.append('강호동')
print('st : {}'.format(st))
print('st의 길이 : {}'.format(len(st)))
print('st의 마지막 인덱스 : {}'.format(len(st) - 1))



scores = [['국어', 58], ['영어', 77], ['수학', 89], ['과학', 99], ['국사', 50]]
scores.append(['수학', 96])
print(f'scores : {scores}')

for sub, sco in scores:
    print(f'과목 : {sub}, 점수: {sco}')

