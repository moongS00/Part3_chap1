# 나와 친구가 좋아하는 번호를 합치되 번호가 중복되지 않게 하는 프로그램

my_num = [1, 3, 5, 6, 7]
fr_num = [2, 3, 5, 8, 10]

print(f'my_num ; {my_num}')
print(f'fr_num ; {fr_num}')

add_list = my_num + fr_num
print(f'add_list : {add_list}')

res = []
for num in add_list:
    if num not in res:
        res.append(num)

print(f'res : {res}')