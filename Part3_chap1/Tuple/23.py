# 퓨틀의 길이
st = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
sl = len(st)
print(f'길이 : {sl}')



# 반복문과 함께라면 아이템 조회 가능
n = 0
while n < sl:
    print('{} : {}'.format(n, st[n]))
    n += 1
