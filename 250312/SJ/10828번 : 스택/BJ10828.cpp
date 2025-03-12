#include <iostream>
#include <string>
#include <stack>
using namespace std;



int main() {
	int n;
	
	cin >> n; 
	stack <int> k;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;

		if (s == "push") {
			int n;
			cin >> n;
			k.push(n);
		}
		else if (s == "pop") {
			if (k.empty() == 1) {
				cout << -1 << endl;
			}
			else {
				cout << k.top() << endl;
				k.pop();
			}
			
		}
		else if (s == "size") {
			cout << k.size() << endl;
		}
		else if (s == "empty") {
			cout << k.empty() << endl;
		}
		else if (s == "top") {
			if (k.empty() == 1) {
				cout << -1 << endl;
			}else cout << k.top() << endl;
			
		}

	}


}