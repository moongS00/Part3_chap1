# 사용자가 입력한 일정을 삭제하는 프로그램

my_list = ['마켓팅 회의', '회의록 정리',  '점심 약속',  '월간 업무 보고',  '치과 방문',  '마트 장보기']
print(f'일정 : {my_list}')

re_i = input('삭제 대상 입력 : ')
my_list.remove(re_i)
print(f'일정 : {my_list}')