#include <iostream>
#include <deque>
#include <string>
#include <sstream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    while (T--) {
        string p;
        int n;
        string arrStr;
        cin >> p >> n >> arrStr;

        deque<int> dq;
        string num;
        for (int i = 1; i < arrStr.size(); i++) {
            if (isdigit(arrStr[i])) {
                num += arrStr[i];
            }
            else {
                if (!num.empty()) {
                    dq.push_back(stoi(num));
                    num.clear();
                }
            }
        }

        bool isReversed = false, error = false;

        for (char c : p) {
            if (c == 'R') {
                isReversed = !isReversed;
            }
            else if (c == 'D') {
                if (dq.empty()) {
                    error = true;
                    break;
                }
                if (isReversed)
                    dq.pop_back();
                else
                    dq.pop_front();
            }
        }

        if (error) {
            cout << "error\n";
        }
        else {
            cout << "[";
            if (!dq.empty()) {
                if (isReversed) {
                    for (auto it = dq.rbegin(); it != dq.rend(); ++it) {
                        if (it != dq.rbegin()) cout << ",";
                        cout << *it;
                    }
                }
                else {
                    for (auto it = dq.begin(); it != dq.end(); ++it) {
                        if (it != dq.begin()) cout << ",";
                        cout << *it;
                    }
                }
            }
            cout << "]\n";
        }
    }

    return 0;
}
