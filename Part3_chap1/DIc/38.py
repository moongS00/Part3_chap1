# in / not in : key값 존재 유무 판단
mInfo = {}
mInfo['이름'] = '홍길동'
mInfo['전공'] = '통계'
mInfo['학년'] = 4
mInfo['주소'] = '서울'
mInfo['취미'] = ['요리', '여행']

print('이름' in mInfo)
print('전공' in mInfo)
print('학년' in mInfo)
print('주소' in mInfo)
print('메일' in mInfo)

# len() : 딕셔너리 길이 출력
print()
print(f'len(mInfo) : {len(mInfo)}')


# clear() : 모든 아이템 삭제
print()
mInfo.clear()
print(f'mInfo : {mInfo}')