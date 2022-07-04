# 오름차순으로 정렬되어있는 숫자들에 사용자가 입력한 정술를 추가하는 프로그램을 만들어보자

numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
input_num = int(input('숫자 입력 : '))
insert_idx = 0

for idx, number in enumerate(numbers):
    print(idx, number)

    if insert_idx == 0 and number > input_num:
        insert_idx = idx

numbers.insert(insert_idx, input_num)
print(numbers)
