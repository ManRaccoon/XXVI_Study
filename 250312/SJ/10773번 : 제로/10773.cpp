#include <iostream>
#include <vector>
using namespace std;

int main() {

	int k;
	cin >> k;
	vector <int> v;
	int answer = 0;
	for (int i = 0; i < k; i++) {
		int n;
		cin >> n;

		if (v.size() > 0 && n == 0) {
			v.pop_back();
		}
		else {
			v.push_back(n);
		}


	}
	for (auto num : v) {
		answer += num;
	}

	cout << answer << endl;

}
