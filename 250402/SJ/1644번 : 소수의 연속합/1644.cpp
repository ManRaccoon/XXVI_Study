#include <iostream>
#include <vector>
using namespace std;



int main() {

	int n;
	cin >> n;

	
	if (n == 1) {
		cout << 0; 
		return 0;
	}

	vector <int> v(n + 1, 1);
	vector <int >prime;

	for (int i = 2; i * i< n+1; i++) {

		if (v[i] == 1) {
			for (int j = 2; i * j < n + 1; j++) {
				v[i * j] = 0;
			}
		}
	}

	for (int i = 2; i < v.size(); i++) {
		if (v[i] == 1) {
			prime.push_back(i);

		}
	}
	int ans = 0;
	int left = 0, right = 0, sum = 0;

	
	while (true) {
		if (sum >= n) {
			if (sum == n) ans++;
			sum -= prime[left++];
		}
		else {
			if (right == prime.size()) break;
			sum += prime[right++];
		}
	}

	cout << ans << endl;


	
}
