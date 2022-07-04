# keys(), values() : 전체 key값과 value값을 조회할 수 있다.

mInfo = {}
mInfo['이름'] = '홍길동'
mInfo['전공'] = '통계'
mInfo['학년'] = 4
mInfo['주소'] = '서울'
mInfo['취미'] = ['요리', '여행']

ks = mInfo.keys()
vs = mInfo.values()
items = mInfo.items()

print(f'ks : {ks}')
print(f'ks type : {type(ks)}')
print()
print(f'vs : {vs}')
print(f'vs type : {type(vs)}')
print()
print(f'items : {items}')
print(f'items type : {type(items)}')

# 리스트로 변환하기
ks = list(ks)
vs = list(vs)
items = list(items)
print()
print(f'ks : {ks}')
print(f'ks type : {type(ks)}')
print()
print(f'vs : {vs}')
print(f'vs type : {type(vs)}')
print()
print(f'items : {items}')
print(f'items type : {type(items)}')


# for문을 이용한 조회
for i in mInfo.keys():
    print(f'{i} : {mInfo[i]}')