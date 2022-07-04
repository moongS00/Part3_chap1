# pop()  : 마지막 인덱스에 해당하는 아이템을 삭제할 수 있다
# pop(n) : n인덱스에 해당하는 아이템을 삭제할 수 있다 / 뒤에있는 자료의 인덱스는 하나씩 당겨진다

st = ['김성예', '신경도', '박기준', '최승철', '황동석']
print(f'st : {st}')
print(f'st length : {len(st)}')

st.pop()
print(f'st : {st}')
print(f'st length : {len(st)}')

st = ['김성예', '신경도', '박기준', '최승철', '황동석']
rv = st.pop(1)
print(f'st : {st}')
print(f'st length : {len(st)}')
print(f'pop()로 지운 값 : {rv}')