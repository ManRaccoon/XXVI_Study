https://www.acmicpc.net/problem/10814

### 문제 설명
회원 수 N과 회원의 나이, 이름이 주어지는데 이를 나이 순, 나이가 같으면 가입한 순으로 출력한다.

### 문제 해결
정렬 알고리즘 중에서 stable sort라고 정렬이 되었을 때 같은 값이 있을 때, 들어온 순서가 변하지 않는 sorting 방법이 있다.

학습을 진행할 때 pair자료구조를 이용해 vector를 만들어 입력을 받고,

algorithm라이브러리에서 stable_sort라는 함수를 사용하여 학습한 vector를 정렬하여 문제를 풀었다.

이 때 cmp라는 함수를 이용해서 sorting하는 방식을 지정해줄 수 있다.

코드의 return 값의 괄호를 반대로 하면 내림차순으로 진행되는 stable_sort가 된다.
