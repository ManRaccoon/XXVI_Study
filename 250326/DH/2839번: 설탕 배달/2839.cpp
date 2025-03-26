#include <iostream>
using namespace std;
int main()
{
    int N;
    cin >> N;
    int result;
    result = N / 5;
    N %= 5;
    if (N == 0)
        cout << result << endl;
    else if (N == 1 && result > 0)
        cout << result + 1 << endl;
    else if (N == 2 && result > 1)
        cout << result + 2 << endl;
    else if (N == 3)
        cout << result + 1 << endl;
    else if (N == 4 && result > 0)
        cout << result + 2 << endl;
    else
        cout << -1 << endl;
}
