#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E;
    cin >> V >> E;

    int start;
    cin >> start;

    vector<vector<pair<int, int>>> graph(V + 1);
    vector<int> dist(V + 1, INF);

    // 간선 정보 입력
    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back(make_pair(v, w));
    }

    // 최소 힙 priority_queue 선언
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push(make_pair(0, start));

    while (!pq.empty()) {
        int cur_dist = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (cur_dist > dist[u]) continue;

        for (size_t i = 0; i < graph[u].size(); ++i) {
            int v = graph[u][i].first;
            int cost = graph[u][i].second;

            if (dist[v] > dist[u] + cost) {
                dist[v] = dist[u] + cost;
                pq.push(make_pair(dist[v], v));
            }
        }
    }

    // 결과 출력
    for (int i = 1; i <= V; ++i) {
        if (dist[i] == INF)
            cout << "INF\n";
        else
            cout << dist[i] << "\n";
    }

    return 0;
}
