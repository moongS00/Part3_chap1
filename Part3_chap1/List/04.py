# 리스트의 길이 : 리스트에 저장된 아이템 개수

st = ['김성예', '신경도', '박기준', '최승철', '황동석']
print(len(st))

# len()과 반복문을 이용하면 리스트의 아이템 조회가 가능하다
for i in range(len(st)):
    print('i : {}'.format(i))
    print('st[{}] : {}'.format(i, st[i]))


# while문 사용
n = 0
sLen = len(st)

while n < sLen:
    print('n : {}'.format(n))
    print('st[{}] : {}'.format(n, st[n]))
    n += 1