import heapq

def schedule_lectures(offers):
    # 비어있는 리스트면 바로 0 반환
    if not offers:
        return 0
    
    # 날짜 순으로 내림차순 정렬
    offers.sort(key=lambda x: x[1])
    
    # 최대 날짜 찾기
    max_day = offers[-1][1]
    
    # 우선순위 큐(최소 힙) 사용
    pq = []
    total_pay = 0
    
    # 마지막 날부터 첫째 날까지 역순으로 진행
    for day in range(max_day, 0, -1):
        # 현재 날짜 이하의 강연을 모두 우선순위 큐에 추가
        while offers and offers[-1][1] >= day:
            p, d = offers.pop()
            heapq.heappush(pq, -p)  # 최대 힙을 구현하기 위해 음수로 저장
        
        # 현재 날짜에 가능한 강연 중 가장 페이가 높은 것을 선택
        if pq:
            total_pay -= heapq.heappop(pq)  # 음수로 저장했으므로 빼기
    
    return total_pay

# 입력 처리
n = int(input())
offers = []
for _ in range(n):
    p, d = map(int, input().split())
    offers.append((p, d))

# 결과 출력
print(schedule_lectures(offers))
