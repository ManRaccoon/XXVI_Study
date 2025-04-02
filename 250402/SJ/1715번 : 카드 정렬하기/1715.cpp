#include <iostream>
#include <queue>
using namespace std;




int main() {

	int n; 
	cin >> n;
	priority_queue<int, vector <int> , greater<int>> pq;
	int sum = 0;

	while (n--) {
		int temp;
		cin >> temp;
		pq.push(temp);

	}

	while (pq.size() != 1) {
		int n1 = pq.top();
		pq.pop();
		int n2 = pq.top();
		pq.pop();
		sum += (n1 + n2);
		pq.push(n1 + n2);

	}

	cout << sum << endl;

}
