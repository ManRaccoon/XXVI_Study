#include <iostream>
#include <string>
using namespace std;

int main() {
  string raw;
  cin >> raw;
  int result = 0;
  string tmp = "";
  bool flag = false;
  for (int i = 0; i < raw.length(); i++) {
    if (raw[i] == '-') {
      if (flag == false) {
        result += stoi(tmp);
        flag = true;
        tmp = "";
      } else {
        result -= stoi(tmp);
        tmp = "";
      }
    } else if (raw[i] == '+') {
      if (flag == false) {
        result += stoi(tmp);
        tmp = "";
      } else {
        result -= stoi(tmp);
        tmp = "";
      }
    } else
      tmp += raw[i];
  }
  if (flag == false)
    result += stoi(tmp);
  else
    result -= stoi(tmp);
  cout << result << endl;
}
