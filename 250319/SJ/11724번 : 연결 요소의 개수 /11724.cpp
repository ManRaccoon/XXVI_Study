#include<iostream>
#include <queue>
#include <vector>
using namespace std;

vector <int> v[1000];


void bfs(int n, int m) {

	bool* visited = new bool[n+1]();

	

	queue  <int> q;
	

	int c = 0;

	for (int j = 1; j <= n; j++) {


		if (!visited[j]) {
			q.push(j);
			visited[j] = true;
			c++;
		}
		while (!q.empty()) {
			int x = q.front();


			q.pop();

			for (int i = 0; i < v[x].size(); i++) {
				int y = v[x][i];
				if (!visited[y]) {
					q.push(y);
					visited[y] = true;

				}

			}


		}
	}


	delete[] visited;
	cout << c << endl;
}


int main() {

	int n, m;
	cin >> n >> m;


	for (int i = 0; i < m; i++) {
		int f, e;
		cin >> f >> e;
		
		v[f].push_back(e);
		v[e].push_back(f);

	}

	bfs(n, m);
}
