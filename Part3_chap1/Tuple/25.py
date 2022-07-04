# 튜플 슬라이싱 : [n:m]
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('원본 : {}'.format(a))
print('[2:4] : {}'.format(a[2:4]))
print('[:4] : {}'.format(a[:4]))
print('[2:] : {}'.format(a[2:]))
print('[2:-2] : {}'.format(a[2:-2]))

# 슬라이싱 단계 설정
print('단계설정')
print('[2:10:2] : {}'.format(a[2:10:2]))
print('[:4:2] : {}'.format(a[:4:2]))
print('[2::2] : {}'.format(a[2::2]))
print('[2:-2:2] : {}'.format(a[2:-2:2]))

# 리스트처럼 슬라이싱을 이용한 아이템 변경은 불가능

# slice() 사용 가능
print('slice()')
print('slice(2, 4) : {}'.format(a[slice(2, 4)]))
print('slice(4) : {}'.format(a[slice(4)]))
print('slice(2, len(a) : {}'.format(a[slice(2, len(a))]))
print('slice(2, -2) : {}'.format(a[slice(2, -2)]))


