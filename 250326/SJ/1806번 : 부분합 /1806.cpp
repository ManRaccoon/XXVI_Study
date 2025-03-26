#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>  
using namespace std;

int main() {
    int n, s;
    cin >> n >> s;

    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int l = 0;
    int r = 0;
    int sum = 0;
    int answer = INT_MAX;

    while (r < n) {
        sum += v[r];

        while (sum >= s) {
            answer = min(answer, r - l + 1);
            sum -= v[l];
            l++;
        }

        r++;
    }

    if (answer == INT_MAX) answer = 0;
    cout << answer << endl;

    return 0;
}
