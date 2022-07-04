# in / not in : 아이템의 존재 유무 판단

st = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
name = input('학생 이름 입력 : ')

if name in st:
    print('{} 학생은 우리반 학생입니다.'.format(name))
else:
    print('{} 학생은 우리반 학생이 아닙니다.'.format(name))




# 문자열에서도 사용 가능
pstr = '파이썬은 1991년 네덜란드계 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, ' \
       '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑 대화형 언어이다. ' \
       '파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'

print('{} : {}'.format('Python', 'Python' in pstr))
print('{} : {}'.format('python', 'python' in pstr))

print('{} : {}'.format('파이썬', '파이썬' in pstr))
print('{} : {}'.format('파이선', '파이선' in pstr))

print('{} : {}'.format('귀도', '귀도' in pstr))
print('{} : {}'.format('객체지향적', '객체지향적' in pstr))
