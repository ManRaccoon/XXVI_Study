def solve():
    n = int(input())
    guilt = list(map(int, input().split()))  # 유죄 지수
    
    # 반응 배열 R[i][j]: i가 죽으면 j의 유죄지수가 R[i][j]만큼 변함
    R = []
    for i in range(n):
        R.append(list(map(int, input().split())))
    
    eunjin = int(input())  # 은진이(마피아)의 번호
    max_nights = 0
    
    # 백트래킹을 위한 함수
    def backtrack(alive, guilt_scores, nights):
        nonlocal max_nights
        
        # 살아있는 사람 수 확인
        alive_count = sum(alive)
        
        # 마피아가 죽었으면 종료
        if not alive[eunjin]:
            return
        
        # 마피아만 남았으면 승리
        if alive_count == 1:
            max_nights = max(max_nights, nights)
            return
        
        # 짝수 명이면 밤 (마피아가 죽일 차례)
        if alive_count % 2 == 0:
            # 마피아가 죽일 수 있는 모든 사람을 시도
            for i in range(n):
                if alive[i] and i != eunjin:  # 살아있고 마피아가 아닌 사람
                    # i를 죽이기
                    alive[i] = False
                    
                    # 유죄지수 업데이트
                    original_guilt = guilt_scores[:]
                    for j in range(n):
                        if alive[j]:
                            guilt_scores[j] += R[i][j]
                    
                    # 다음 상태로 재귀 호출 (밤 수 증가)
                    backtrack(alive, guilt_scores, nights + 1)
                    
                    # 되돌리기 (백트래킹)
                    alive[i] = True
                    guilt_scores[:] = original_guilt
        
        # 홀수 명이면 낮 (시민들이 죽일 차례)
        else:
            # 유죄지수가 가장 높은 사람 찾기 (같으면 번호가 작은 사람)
            max_guilt = -float('inf')
            target = -1
            
            for i in range(n):
                if alive[i]:
                    if guilt_scores[i] > max_guilt or (guilt_scores[i] == max_guilt and (target == -1 or i < target)):
                        max_guilt = guilt_scores[i]
                        target = i
            
            # 마피아가 죽게 되면 게임 종료
            if target == eunjin:
                max_nights = max(max_nights, nights)
                return
            
            # target을 죽이고 다음 상태로 진행
            alive[target] = False
            
            # 유죄지수 업데이트
            original_guilt = guilt_scores[:]
            for j in range(n):
                if alive[j]:
                    guilt_scores[j] += R[target][j]
            
            backtrack(alive, guilt_scores, nights)
            
            # 복원
            alive[target] = True
            guilt_scores[:] = original_guilt
    
    # 초기 상태 설정
    alive = [True] * n
    
    # 백트래킹 시작
    backtrack(alive, guilt[:], 0)
    
    return max_nights

print(solve())
