#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    long long min, max;
    cin >> min >> max;

    long long size = max - min + 1;
    vector<bool> isSquareFree(size, true);  

    for (long long i = 2; i * i <= max; i++) {
        long long square = i * i;

        
        long long start = ((min + square - 1) / square) * square;

        for (long long j = start; j <= max; j += square) {
            isSquareFree[j - min] = false;
        }
    }

    int answer = 0;
    for (int i = 0; i < size; i++) {
        if (isSquareFree[i]) answer++;
    }

    cout << answer << endl;
    return 0;
}
