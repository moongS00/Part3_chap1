# [n:m] : 인덱스 n부터 m-1까지 리스트 슬라이싱

st = ['0.홍길동', '1.박찬호', '2.이용규', '3.강호동', '4.박승철', '5.김지은']
print(f'st : {st}')
print(f'st[2:4] : {st[2:4]}')
print(f'st[:4] : {st[:4]}')
print(f'st[2:] : {st[2:]}')
print(f'st[2:-2] : {st[2:-2]}')  # -2: 뒤에서 2번째 까지


# 문자열 슬라이싱도 가능
str = 'abcdefghijklmnopqrstuvwxyz'
print('str len : {}'.format(len(str)))
print('str[2:4] : {}'.format(str[2:4]))
print('str[:4] : {}'.format(str[:4]))
print('str[2:] : {}'.format(str[2:]))
print('str[2:-2] : {}'.format(str[2:-2]))
print('str[-5:-2] : {}'.format(str[-5:-2]))



# 슬라이싱 단계 설정 가능
num = [2, 50, 0.12, 1, 9, 7, 14, 35, 100, 3.14]
print('num[:4:2] : {}'.format(num[:4:2]))
print('num[2::2] : {}'.format(num[2::2]))
print('num[2:-2:2] : {}'.format(num[2:-2:2]))


# 슬라이싱을 이용해 아이템 변경 가능
li = ['0.홍길동', '1.박찬호', '2.이용규', '3.강호동', '4.박승철', '5.김지은']
print(f'li :{li}')
li[1:4] = [1, 2, 3]
print(f'li :{li}')

# slice() 함수 사용 가능
st = ['0.홍길동', '1.박찬호', '2.이용규', '3.강호동', '4.박승철', '5.김지은']
print(f'st : {st}')
print('st : {}'.format(st[slice(2, 4)]))
print('st : {}'.format(st[slice(4)]))
print('st : {}'.format(st[slice(2, len(st))]))
print('st : {}'.format(st[slice(2, len(st)-2)]))
print('st : {}'.format(st[slice(len(st)-5, len(st)-2)]))
print('st : {}'.format(st[slice(len(st)-5, len(st)-2)]))