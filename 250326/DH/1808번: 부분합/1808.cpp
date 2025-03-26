#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N, S;
  cin >> N >> S;

  vector<int> numbers(N);
  for (int i = 0; i < N; i++) {
    cin >> numbers[i];
  }

  int st_idx = 0, ed_idx = 0, acc = 0;
  int minlen = N + 1;

  while (true) {
    if (acc >= S) {
      minlen = min(minlen, ed_idx - st_idx);
      acc -= numbers[st_idx++];
    } else if (ed_idx == N) {
      break;
    } else {
      acc += numbers[ed_idx++];
    }
  }

  if (minlen == N + 1)
    cout << 0 << endl;
  else
    cout << minlen << endl;

  return 0;
}
