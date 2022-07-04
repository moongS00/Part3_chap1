# 최고, 최저점 삭제 후 총점과 평균 출력


ps = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print('점수원본 : {}'.format(ps))
print(type(ps))
ps = list(ps)

ps.sort()
print('정리 후 : {}'.format(ps))

ps.pop()
ps.pop(0)
print('삭제 후 : {}'.format(ps))
print(type(ps))

sum = 0
for i in ps:
    sum += i

avg = sum / len(ps)
print('총합 : %.2f' %sum)
print('평균 : %.2f' %avg)


