https://www.acmicpc.net/problem/11724

#백준 11724번 연결 요소의 개수 (실버 2티어)
##문제 설명
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
##해결 접근법

1. 입력 양방향 그래프여서 vector에 , 양뱡향으로 넣어주었다. 예를들어 2,1 이면 1과 2는 연결되어 있으므로 1,2도
  백터에 넣어주었다.

2. 그리고 전역으로 벡터를 선언해서, BFS 서치가 안된 노드들을 따로 BFS를 돌렸다. 
