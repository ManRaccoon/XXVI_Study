백준 1715번 카드 정렬하기 문제를 풀어보았다.

Priority_queue를 쓰면 vector에서 정렬까지 할 수 있어 매우 유용해보여서, 공부해보려고 문제를 풀어보았다.

하지만 priority queue를 알아보고 구현하지 않아서 처음에는 오름차순으로 정리되는줄 알고, 구현을 짰는데, 100이 나와야 하는데

결과값이 계속130이 나왔다.

priority_queue<int, vector <int> , greater<int>> pq;이렇게 짜야 오름차순으로 정리된다고 해서, 고쳤는데,

아직 저기에 vector가 왜 들어가는지 이해하지 못했다. 다음에 공부해서 priority queue를 마스터 하려고 한다.
