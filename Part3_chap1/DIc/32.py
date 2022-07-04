# 딕셔너리 : key, value를 이용한 자료 관리
# key, value에는 숫자, 문자(열), 논리, 컨테이너형 모두 올수 있다
# 단, key에 immutable 값은 올수 있지만 mutable값은 올수 없다

st = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}
memInfo = {'이름':'홍길동', '메일':'fjfj@gmail.com', '학년':3, '취미':['농구', '게임']}
sd1 = {'이름':'홍길동', '메일':'fjfj@gmail.com', '학년':3}
sd2 = {'이름':'박찬호', '메일':'dskw@gmail.com', '학년':2}
sd3 = {'이름':'이ㅛㅇ규', '메일':'djfjfi@gmail.com', '학년':1}

stInfo = {1:sd1, 2:sd2, 3:sd3}
print(f'st : {st}')
print(f'memInfo : {memInfo}')
print(f'sd1 : {sd1}')
print(f'stInfo : {stInfo}')
