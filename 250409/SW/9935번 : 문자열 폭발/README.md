# 백준 9935번 문자열 폭발 (골드 4티어)

## 문제 설명

문자열 S와 폭발 문자열 B가 주어질 때, S 내에서 B가 등장할 때 마다 해당 문자열을 제거하고, 폭발로 인해 문자열이 합쳐질 경우 새로운 B가 만들어질 수 있다. 모든 폭발 과정이 완료된 뒤 남은 문자열을 출력해야한다.

## 해결 접근법

1. 문자열 S를 순회하면서 하나씩 스택에 넣었다.

2. 스택에 새 문자를 추가할 때마다 마지막에 폭발 문자열 B가 있는지 확인했다.

3. 스택의 길이가 폭발 문자열보다 크거나 같으면, 스택의 마지막 부분이 폭발 문자열과 동일한지 확인하고, 같다면 스택의 마지막 부분을 제거했다.

4. 문자열 S를 모두 순회한 후 스택에 남아있는 문자들이 있다면 결과로 내보내고 스택이 비어있다면 "FRULA"를 출력하도록 하였다.

## 어려웠던 점

폭발 문자열이 아주 짧거나, S 전체가 폭발 문자열로만 이루어진 경우 등 다양한 예외 상황을 처리할 수 있도록 해야했다.
