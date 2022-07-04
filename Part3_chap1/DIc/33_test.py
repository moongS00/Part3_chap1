# 내 정부 저장 후 출력

minfo = {'이름':'홍길동', '전공':'통계', '학년':4, '주소':'서울', '취미':['축구','요리']}

print('이름: {}'.format(minfo['이름']))
print('전공: {}'.format(minfo['전공']))
print('학년: {}'.format(minfo['학년']))
print('주소: {}'.format(minfo['주소']))
print('취미: {}'.format(minfo['취미']))
print()
print('이름: {}'.format(minfo.get('이름')))
print('전공: {}'.format(minfo.get('전공')))
print('학년: {}'.format(minfo.get('학년')))
print('주소: {}'.format(minfo.get('주소')))
print('취미: {}'.format(minfo.get('취미')))