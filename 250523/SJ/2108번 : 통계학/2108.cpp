#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);

    vector<int> freq(8001, 0);

    long long sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
        freq[a[i] + 4000]++;
    }


    double avg = double(sum) / n;
    int mean = (int)round(avg);


    sort(a.begin(), a.end());
    int median = a[n/2];

    int maxf = 0;
    for (int f : freq) {
        if (f > maxf) maxf = f;
    }
    vector<int> modes;
    for (int i = 0; i < (int)freq.size(); i++) {
        if (freq[i] == maxf) {
            modes.push_back(i - 4000);
        }
    }
    int mode = (modes.size() > 1 ? modes[1] : modes[0]);


    int range = a.back() - a.front();

    cout << mean << "\n";
    cout << median << "\n";
    cout << mode << "\n";
    cout << range << "\n";

    return 0;
}
