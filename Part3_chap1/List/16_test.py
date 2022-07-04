# 암호 해독 프로그램 만들기

secret = '27156231'

s_list = []
r_list = ''


for ch in secret:
    s_list.append(int(ch))

s_list.reverse()
print(f's_list : {s_list}')


val = s_list[0] * s_list[1]
s_list.insert(2, val)

val = s_list[3] * s_list[4]
s_list.insert(5, val)

val = s_list[6] * s_list[7]
s_list.insert(8, val)

val = s_list[9] * s_list[10]
s_list.insert(11, val)


print(f's_list : {s_list}')



