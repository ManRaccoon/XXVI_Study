#include <iostream>
#include <vector>
#include<algorithm>
#include<climits>
using namespace std;

int main() {

	int n;
	cin >> n;
	vector <int > v(n);
	
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}


	sort(v.begin(), v.end());
	

	int left = 0; 

	int right = n - 1;
	int minSum = INT_MAX;
	int al = 0;
	int ar = 0;

	while (left < right) {
		int sum = v[left] + v[right];

		if (abs(sum) < minSum) {
			minSum = abs(sum);
			al = left;
			ar = right;
		}

		if (sum == 0) break;

		if (sum > 0) right--;
		else left++;

		
	}


	cout << v[al] << " " << v[ar] << endl;
	
}
