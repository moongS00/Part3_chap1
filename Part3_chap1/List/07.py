# while 문을 이용한 리스트 조회

cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

# 1.
print('<1>')
n1 = 0
while n1 < len(cars):
    print(cars[n1])
    n1 += 1


# 2.
print('<2>')
n2 = 0
flag = True
while flag:
    print(cars[n2])
    n2 += 1

    if n2 == len(cars):
        flag = False


# 3.
print('<3>')
n3 = 0
while True:
    print(cars[n3])
    n3 += 1

    if n3 == len(cars):
        break


# 4.
st = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

n4 = 0
while n4 < len(st):
    print('{}학급 학생 수 : {}'.format(st[n4][0], st[n4][1]))
    n4 += 1