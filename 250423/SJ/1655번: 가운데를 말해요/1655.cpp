#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    priority_queue<int> left; 
    priority_queue<int, vector<int>, greater<int>> right; 

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;

        if (left.empty() || num <= left.top()) {
            left.push(num);
        }
        else {
            right.push(num);
        }

       
        if (left.size() > right.size() + 1) {
            right.push(left.top());
            left.pop();
        }
        else if (right.size() > left.size()) {
            left.push(right.top());
            right.pop();
        }

        cout << left.top() << endl;
    }

    return 0;
}
