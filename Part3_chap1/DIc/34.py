# 딕셔너리 추가

mInfo = {}
mInfo['이름'] = '홍길동'
mInfo['전공'] = '통계'
mInfo['학년'] = 4
mInfo['주소'] = '서울'
mInfo['취미'] = ['요리', '여행']

print(mInfo)

# 추가하려는 키가 이미 있다면 기존 값이 변경된다
mInfo['전공'] = '컴퓨터공학'
print(mInfo)