#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int num, result = 1, edTime, i;
    cin >> num;
    pair<int, int> arr[num];
    for (i = 0; i < num; i++) // first:edTime
    {
        int st, ed;
        cin >> st >> ed;
        arr[i].first = ed;
        arr[i].second = st;
    }
    sort(arr, arr + num);
    edTime = arr[0].first;
    for (i = 1; i < num; i++)
    {
        if (arr[i].second >= edTime)
        {
            result++;
            edTime = arr[i].first;
        }
    }
    cout << result << endl;
