# for문을 이용한 list조회 : for문을 이용면 리스트의 아이템을 자동으로 참조할 수 있다

cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

for i in range (len(cars)):
    print(cars[i])

for n in cars:
    print(n)


# for문을 이용하면 리스트 내부의 또 다른 리스트의 아이템을 조회할 수 있다.

st = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

for i in range(len(st)):
    print('{}학급 학생수 : {}'.format(st[i][0], st[i][1]))

for classNo, cnt in st:
    print('{}학급 학생 수 : {}'.format(classNo, cnt))