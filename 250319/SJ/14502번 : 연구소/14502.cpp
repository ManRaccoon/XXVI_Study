#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int fn(int n, int m, vector<int> v[16]) {
    int c = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (v[i][j] == 0) {
                c++;
            }
        }
    }
    return c;
}

int bfs(int n, int m, vector<pair<int, int>> w, vector<int> v[16]) {
    queue<pair<int, int>> q;

    bool** visited = new bool* [n];
    for (int i = 0; i < n; i++) {
        visited[i] = new bool[m]();
    }

    for (int i = 0; i < 3; i++) {
        int x = w[i].first;
        int y = w[i].second;
        v[y][x] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (v[i][j] == 2) {
                q.push(make_pair(j, i));
                visited[i][j] = true;
            }
            if (v[i][j] == 1) {
                visited[i][j] = true;
            }
        }
    }

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        int dx[4] = { 1, 0, -1, 0 };
        int dy[4] = { 0, -1, 0, 1 };

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                if (!visited[ny][nx] && v[ny][nx] == 0) {
                    q.push(make_pair(nx, ny));
                    visited[ny][nx] = true;
                    v[ny][nx] = 2;
                }
            }
        }
    }

    int k = fn(n, m, v);

   
    for (int i = 0; i < n; i++) {
        delete[] visited[i];
    }
    delete[] visited;

    return k;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> v[16];
    vector<pair<int, int>> v0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int x;
            cin >> x;
            if (x == 0) {
                v0.push_back(make_pair(j, i));
            }
            v[i].push_back(x);
        }
    }

    int max = 0;
    for (int i = 0; i < v0.size() - 2; i++) {
        for (int j = i + 1; j < v0.size() - 1; j++) {
            for (int k = j + 1; k < v0.size(); k++) {
                vector<pair<int, int>> w = { v0[i], v0[j], v0[k] };

                
                vector<int> v_copy[16];
                for (int l = 0; l < n; l++) {
                    v_copy[l] = v[l];
                }

                int x = bfs(n, m, w, v_copy);

                if (max < x) {
                    max = x;
                }
            }
        }
    }
    cout << max << endl;

    return 0;
}
