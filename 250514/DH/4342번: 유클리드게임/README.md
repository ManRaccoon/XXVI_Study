https://www.acmicpc.net/problem/4342

### 문제 설명

a > b인 a, b가 주어지는데 두 플레이어는 두 행동 중 하나를 선택해야 한다.

1. a = a mod b로 만든다
2. a = a - k * b 형태로 만든다. 단, k \geq 1이고 a - k \cdot b \geq 0이어야 한다.

이후 두 수를 다시 정렬해서 a > b가 되도록 유지하며 다음 턴을 진행한다.

이 때 첫 번째 행동하는 플래어가 이기는지 지는지 판별하여 "win" 또는 "lose"를 출력한다.

또한 끝났을 경우에는 0, 0이 출력된다.

### 문제 해결

유클리드 호제법 기반의 게임이론 문제이다.

a > b일 때, a / b >= 2가 되는 순간이 존재하면 이기고 아니면 지게 된다.

이러한 로직으로 while문을 지속하면 결과가 나온다.
