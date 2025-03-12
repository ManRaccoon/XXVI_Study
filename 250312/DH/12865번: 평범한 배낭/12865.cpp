#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  vector<pair<int, int>> BAG(N);
  vector<vector<int>> DP(K+1, vector<int>(N+1, 0));

  for (int i = 0; i < N; i++) {
    cin >> BAG[i].first >> BAG[i].second;
  }

  for (int i=1; i<=K; i++) { // run DP
    for (int j=1; j<=N; j++) {
      if (i < BAG[j-1].first)
        DP[i][j] = DP[i][j - 1];
      else
        DP[i][j] = DP[i][j-1] < DP[i-BAG[j-1].first][j-1] + BAG[j-1].second ? DP[i-BAG[j-1].first][j-1] + BAG[j-1].second : DP[i][j-1];
    }
  }

  cout << DP[K][N] << endl;
