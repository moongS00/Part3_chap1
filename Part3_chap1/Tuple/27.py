# 퓨틀 아이템 정렬 : 리스트로 변환 후 정렬

f = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print(f'f : {f}, type : {type(f)}')

f = list(f)
f.sort(reverse=False)
print(f'f : {f}, type : {type(f)}')

f = tuple(f)
print(f'f : {f}, type : {type(f)}')


# sorted() : 튜플 정렬 가능, 리스트 자료형을 반환
g = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
sg = sorted(g)
print(f'sg : {sg}, type : {type(sg)}')