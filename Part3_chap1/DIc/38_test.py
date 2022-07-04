# 개인정보에 연락처와 주민등록번호가 있다면 삭제하는 코드 작성하기

myInfo = {'이릅': '홍길동', '나이': '30', '연락처': '010-123-456', '주민등록번호': '999999-5555555', '주소': '서울'}
print(f'myInfo : {myInfo}')
delete = ['연락처', '주민등록번호']

for item in delete:
    if(item in myInfo):
        del myInfo[item]

print(f'myInfo : {myInfo}')
