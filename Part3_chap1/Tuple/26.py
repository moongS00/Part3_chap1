# 리스트와 튜플 비교
# 튜플은 리스트와 달리 아이템 추가, 삭제, 변경 불가능

a = [0, 1, 2, 3, 4, 5]
print(a)
a.append(6)  #추가
a[0] = '영'  #변경
a.pop()  #삭제
print(a)

'''
b = (0, 1, 2, 3, 4, 5)
b.append(6)  #추가
b[0] = '영'  #변경
b.pop()  #삭제
'''

# 2. 튜플은 선언 시 괄호 생략이 가능

aa = [0, 1, 2, 3, 4, 5]
bb = 0, 1, 2, 3, 4, 5
print(f'aa : {aa}')
print(f'type(aa) : {type(aa)}')

print(f'bb : {bb}')
print(f'type(bb) : {type(bb)}')


# 3. 리스트와 튜플은 자료형 변환이 가능하다
aa = tuple(aa)
print(f'aa : {aa}')
print(f'type(aa) : {type(aa)}')

bb = list(bb)
print(f'bb : {bb}')
print(f'type(bb) : {type(bb)}')