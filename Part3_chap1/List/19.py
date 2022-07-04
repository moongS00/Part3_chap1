# count() :  특정 아이템의 개수 알아내기
st = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']

print(f'st : {st}')

search = st.count('강호동')
print(f'search : {search}')



# del : 특정 아이템 삭제
del st[1]
print(f'st : {st}')

st = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']
del st[1:3]
print(f'st : {st}')

st = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']
del st[2:]
print(f'st : {st}')

st = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']
del st[:3]
print(f'st : {st}')