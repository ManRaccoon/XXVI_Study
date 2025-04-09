#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> belt(2 * n); 
    vector<bool> robot(n, false); 

    for (int i = 0; i < 2 * n; i++) {
        cin >> belt[i];
    }

    int step = 0;

    while (true) {
        step++;

     
        rotate(belt.rbegin(), belt.rbegin() + 1, belt.rend());
        rotate(robot.rbegin(), robot.rbegin() + 1, robot.rend());
        robot[n - 1] = false;

    
        for (int i = n - 2; i >= 0; i--) {
            if (robot[i] && !robot[i + 1] && belt[i + 1] > 0) {
                robot[i] = false;
                robot[i + 1] = true;
                belt[i + 1]--;
            }
        }
        robot[n - 1] = false; 

      
        if (belt[0] > 0) {
            robot[0] = true;
            belt[0]--;
        }

   
        int zeroCount = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (belt[i] == 0) zeroCount++;
        }

        if (zeroCount >= k) {
            cout << step << endl;
            break;
        }
    }

    return 0;
}
