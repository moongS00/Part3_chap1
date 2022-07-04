# 1. 학생 정보를 입력받아 딕셔너리에 추가
'''
sInfo = {}
sInfo['이름'] = input('이름 입력 : ')
sInfo['학년'] = input('학년 입력 : ')
sInfo['전공'] = input('전공 입력 : ')
sInfo['주소'] = input('주소 입력 : ')

print(f'sInfo : {sInfo}')

        for j in range(1, (i+1)):
'''

# 2. 0부터 10까지의 각각의 정수에 대한 팩토리얼을 딕셔너리에 추가
facdic = {}

for i in range(11):
    if i == 0:
        facdic[i] = 1
    else:
        facdic[i] = facdic[i-1] * i

print(facdic)