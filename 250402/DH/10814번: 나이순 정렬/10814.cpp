#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool cmp(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main()
{
    int num, i;
    vector<pair<int, string>> li;
    cin >> num;
    while (num--)
    {
        int age;
        string name;
        cin >> age >> name;
        li.push_back(make_pair(age, name));
    }
    stable_sort(li.begin(), li.end(), cmp);
    for (i = 0; i < li.size(); i++)
    {
        cout << li[i].first << " " << li[i].second << "\n";
    }
}
