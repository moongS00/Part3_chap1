# extend() : 리스트 연결
# + 연산자로도 연결 가능

a = ['홍길동', '박찬호', '이용규']
b = ['강호동', '박승철', '김지은']

a.extend(b)
print(a)

b.extend(a)
print(b)

c = [1, 2, 4, 5]
d = [10, 50, 80, 90]
cd = c+d
print(cd)