#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> schedule(K);
    for (int i = 0; i < K; ++i) {
        cin >> schedule[i];
    }

    vector<int> plugged; // 현재 꽂혀 있는 기기
    int answer = 0;

    for (int i = 0; i < K; ++i) {
        int now = schedule[i];

        // 이미 꽂혀 있는 경우
        if (find(plugged.begin(), plugged.end(), now) != plugged.end()) continue;

        // 멀티탭에 자리가 있는 경우
        if (plugged.size() < N) {
            plugged.push_back(now);
            continue;
        }

        // 뽑아야 하는 경우
        int farthest = -1;
        int idx_to_remove = -1;

        for (int j = 0; j < plugged.size(); ++j) {
            int next_use = -1;
            for (int k = i + 1; k < K; ++k) {
                if (schedule[k] == plugged[j]) {
                    next_use = k;
                    break;
                }
            }

            if (next_use == -1) { // 다시 안 쓰이는 기기
                idx_to_remove = j;
                break;
            }
            else if (next_use > farthest) { // 가장 나중에 쓰이는 기기
                farthest = next_use;
                idx_to_remove = j;
            }
        }

        plugged[idx_to_remove] = now;
        answer++;
    }

    cout << answer << '\n';
    return 0;
}
