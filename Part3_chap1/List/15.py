# sort() : 리스트 아이템 정렬(오름차순)
# sort(reverse = True) : 내림차순 정렬

a = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
a.sort()
print(f'오름차순 : {a}')
a.sort(reverse = True)
print(f'내림차순 : {a}')

b = [2, 50, 3.14, 66, 95, 2.1]
b.sort()
print(f'오름차순 : {b}')
b.sort(reverse = True)
print(f'내림차순 : {b}')