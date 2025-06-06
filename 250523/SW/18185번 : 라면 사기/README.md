# 백준 18185번 라면 사기 (골드 3티어)

## 문제 설명

N 개의 라면 공장이 있고 1번부터 N번까지 차례대로 번호가 부여되어 있을 때, i번 공장에서 정확하게 Ai개의 라면을 구매하라.

## 해결 접근법 

1. 그리디 알고리즘으로 접근 하였다.

2. 비용 효율성을 분석하니 가능한 한 3개 연속 구매를 최대한 활용, 그 다음 2개 연속 구매 활용, 마지막에 1개씩 구매하는게 좋다고 생각했다.

3. 하지만 이는 틀린 방법이었고 구매한 라면들을 추적해야 최적의 방법을 찾을 수 있었다.

4. i번째 공장부터 시작하여 순차적으로 처리하고 각 단계에서 최적의 선택을 하도록 했다.

5. 특별한 경우인 b < c일 때 c = b로 설정해주어서 AC가 나오도록 하였다.
