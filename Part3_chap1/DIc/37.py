# 딕셔너리 삭제
# 1. del 사용
mInfo = {}
mInfo['이름'] = '홍길동'
mInfo['전공'] = '통계'
mInfo['학년'] = 4
mInfo['주소'] = '서울'
mInfo['취미'] = ['요리', '여행']

print(f'mInfo : {mInfo} \n')

del mInfo['취미']
print(f'mInfo : {mInfo} \n')

del mInfo['주소']
print(f'mInfo : {mInfo} \n')


# 2. pop() 사용
mInfo = {}
mInfo['이름'] = '홍길동'
mInfo['전공'] = '통계'
mInfo['학년'] = 4
mInfo['주소'] = '서울'
mInfo['취미'] = ['요리', '여행']

rt = mInfo.pop('취미')
print(f'mInfo : {mInfo}')
print(f'rt : {rt}')
print(f'rt type: {type(rt)} \n')

rt = mInfo.pop('주소')
print(f'mInfo : {mInfo}')
print(f'rt : {rt}')
print(f'rt type: {type(rt)}')



