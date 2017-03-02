#include<iostream>
#include<string>
using namespace std;

string findsmallestgreater(string & number) {
  int r = -1, l = -1;

  for (int i = number.size()-1;i > 0;i--) {
    for (int j = i-1;j >= 0;j--) {
      if (number[j] < number[i]) {
        r = i;
        l = j;
        break;
      }
    }
    if (r != l) break;
  }

  if (r == l) return "not possible";

 // cout << l << "  "<< r <<endl;

  char temp = number[r];
  number[r] = number[l];
  number[l] = temp;

 // cout << number <<endl;

  for (int i = l+1;i < number.size()-1;i++) {
    r = i;
    char temp = number[r];
    for (int j = i+1;j < number.size();j++) {
      if (number[j] < temp) {
        temp = number[j];
        r = j;
      }
    }
    if (r != i ) {
      number[r] = number[i]; 
      number[i] = temp;
    }
  }

  return number;

}

int main() {

  string s1 = "218765";
  cout << findsmallestgreater(s1)<<endl;
  string s2 = "1234";
  cout << findsmallestgreater(s2)<<endl;
  string s3 = "4321";
  cout<< findsmallestgreater(s3)<<endl;
  string s4 = "534976";
  cout << findsmallestgreater(s4)<<endl;

  return 0;
}
