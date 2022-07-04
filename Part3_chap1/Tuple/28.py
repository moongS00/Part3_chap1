# for문을 이용한 아이템 조회

cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'

for i in cars:
    print(i)



# for문을 이용한 내부 튜플 조회
sc = (1, 19), (2, 20), (3, 22), (4, 18), (5,21)

for cno, ct in sc:
    print('{}학급 학생 수 : {}'.format(cno, ct))