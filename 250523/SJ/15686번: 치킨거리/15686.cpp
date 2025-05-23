#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<pair<int,int>> houses;
vector<pair<int,int>> chickens;
int answer = INT_MAX;


void dfs(int idx, vector<int>& sel) {
    if ((int)sel.size() == M) {
        int sum = 0;

        for (auto& h : houses) {
            int best = INT_MAX;
            for (int ci : sel) {
                auto& c = chickens[ci];
                int d = abs(h.first - c.first) + abs(h.second - c.second);
                best = min(best, d);
            }
            sum += best;
            if (sum >= answer) break;  
        }
        answer = min(answer, sum);
        return;
    }

    for (int i = idx; i < (int)chickens.size(); i++) {
        sel.push_back(i);
        dfs(i + 1, sel);
        sel.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0, x; j < N; j++) {
            cin >> x;
            if (x == 1) houses.emplace_back(i, j);
            else if (x == 2) chickens.emplace_back(i, j);
        }
    }

    vector<int> sel;
    dfs(0, sel);

    cout << answer << "\n";
    return 0;
}
