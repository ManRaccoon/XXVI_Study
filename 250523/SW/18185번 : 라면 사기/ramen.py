n = int(input())
ramen = list(map(int, input().split()))

total_cost = 0
cnt = [0] * n  # i번째 위치에서 2개 연속으로 산 개수

B = 3  # 1개 구매 비용
C = 2  # 추가 비용 (2개: B+C=5, 3개: B+2C=7)

# 첫 번째 공장은 무조건 B원으로 구매
total_cost += B * ramen[0]

for i in range(1, n):
    # i-1번째와 i번째를 묶어서 B+C원(5원)으로 업그레이드
    upgrade_two = min(ramen[i], ramen[i-1])
    ramen[i] -= upgrade_two
    cnt[i] += upgrade_two
    total_cost += C * upgrade_two  # C원 추가 비용
    
    # i-1번째에서 2개 연속으로 산 것과 i번째를 묶어서 B+2C원(7원)으로 업그레이드
    upgrade_three = min(ramen[i], cnt[i-1])
    ramen[i] -= upgrade_three
    total_cost += C * upgrade_three  # C원 추가 비용
    
    # 남은 라면은 B원으로 구매
    total_cost += B * ramen[i]

print(total_cost)
