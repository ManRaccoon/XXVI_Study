def change_switch(switch_list, gender, number):
    # 남학생인 경우
    if gender == 1:
        # 받은 수의 배수인 스위치의 상태를 바꿈
        for i in range(number, len(switch_list), number):
            switch_list[i] = 1 - switch_list[i]  # 0->1, 1->0으로 변경
    
    # 여학생인 경우
    else:
        # 받은 수의 스위치는 항상 바꿈
        switch_list[number] = 1 - switch_list[number]
        
        # 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간 찾기
        left, right = number - 1, number + 1
        
        while left >= 1 and right < len(switch_list) and switch_list[left] == switch_list[right]:
            switch_list[left] = 1 - switch_list[left]
            switch_list[right] = 1 - switch_list[right]
            left -= 1
            right += 1

# 입력 받기
n = int(input())  # 스위치 개수
# 스위치 상태 (0번 인덱스는 사용하지 않음, 1번부터 시작)
switch_status = [0] + list(map(int, input().split()))

students = int(input())  # 학생 수

# 학생 정보 입력 및 처리
for _ in range(students):
    gender, number = map(int, input().split())
    change_switch(switch_status, gender, number)

# 출력 (한 줄에 20개씩)
for i in range(1, n + 1):
    print(switch_status[i], end=" ")
    if i % 20 == 0:
        print()  # 20개마다 줄바꿈
if n % 20 != 0:  # 마지막 줄 추가
    print()
