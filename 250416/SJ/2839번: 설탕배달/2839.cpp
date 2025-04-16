#include <iostream>
#include <queue>
using namespace std;

void findS(int n) {

    queue <int> q;

    int arr[5001] = { 0 };
    int ar[2] = { 3, 5 };
    arr[3] = 1;
    arr[5] = 1;
    q.push(3);
    q.push(5);

    while (!q.empty()) {
        
        
        int x = q.front();
        if (x >= n) {
            break;
        }

        q.pop();


        for (int i = 0; i < 2; i++) {
            
            int nx = x + ar[i];
            if (arr[nx] == 0) {
                arr[nx] = arr[x] + 1;
                q.push(nx);
            }
        }

    }

    if (arr[n]==0) {
        cout << -1 << endl;
    }
    else {
        cout << arr[n] << endl;
    }
}


int main()
{
    int n;
    cin >> n;
    findS(n);

}
