# 나와 친구가 좋아하는 번호를 합치되, 중복되지 않게 하기

mf = (1, 3, 5, 7, 8, 9)
ff = (4, 5, 6, 7, 8, 9)

print(f'내 번호 : {mf}')
print(f'친구 번호 : {ff}')

c = mf + ff
af = ()

for num in c:
    if num not in af:
        af = af + (num, )


print(f'결과: {af}')
