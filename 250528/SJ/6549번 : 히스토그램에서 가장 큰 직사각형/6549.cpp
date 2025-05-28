#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;  

        vector<ll> h(n);
        for (int i = 0; i < n; i++) {
            cin >> h[i];
        }

        stack<int> st;
        ll maxArea = 0;

        for (int i = 0; i <= n; i++) {
          
            ll curH = (i == n ? 0 : h[i]);

          
            while (!st.empty() && curH < h[st.top()]) {
                ll height = h[st.top()];
                st.pop();
                int left = st.empty() ? 0 : (st.top() + 1);
                ll width = i - left;
                maxArea = max(maxArea, height * width);
            }

            st.push(i);
        }

        cout << maxArea << "\n";
    }

    return 0;
}
