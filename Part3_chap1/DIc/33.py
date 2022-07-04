# 1. 딕셔너리 조회: key값을 이용해 value를 조회 (없는 key값을 넣으면 에러 발생)
st = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':['김지은', '박지은']}

print('st[\'s1\'] : {}'.format(st['s1']))
print('st[\'s2\'] : {}'.format(st['s2']))
print('st[\'s3\'] : {}'.format(st['s3']))
print('st[\'s4\'] : {}'.format(st['s4']))
print('st[\'s5\'] : {}'.format(st['s5']))
print('st[\'s5\'][0] : {}'.format(st['s5'][0]))
print('st[\'s5\'][1] : {}'.format(st['s5'][1]))


# 2. get(key)를 이용해서 value조회 가능 (없는 key값을 넣어도 에러 발생 안함)
ct = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':['김지은', '박지은']}
print('ct.get(\'s1\'): {}'.format(ct.get('s1')))
print('ct.get(\'s2\'): {}'.format(ct.get('s2')))
print('ct.get(\'s3\'): {}'.format(ct.get('s3')))
print('ct.get(\'s4\'): {}'.format(ct.get('s4')))
print('ct.get(\'s5\'): {}'.format(ct.get('s5')))
print('ct.get(\'s6\'): {}'.format(ct.get('s6')))
