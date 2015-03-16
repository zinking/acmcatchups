#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>

using namespace std;

class Solution{
public:
  string pre;
  string pos;
  int count;
  Solution(string pre, string pos){
    this->pre = pre;
    this->pos = pos;
    count = 0;
  }

  void solve(){
    decompose(pre,"","",pos);
    cout << cout << endl;
  }

  void decompose(string i, string l, string r, string pos ){
    int n  = i.length();
    int nl = l.length();
    int nr = r.length();
    cout << i << "1: " << l << "2:" << r << "3:" << pos << endl;
    if( n == 1 && nl<=1 && nr<=1 ){
      if( l+r+i == pos ) count++;
    }
    else{
      string subpos = pos.substr(0,n-1);
      string rnode = i.substr(0,1);
      decompose(i.substr(1,n-1), "", subpos);
      decompose(rnode, "", i.substr(1,n-1), subpos);
    }
  }
};




int main()
{
  string pre,pos;
  cin >> pre;
  cin >> pos;
  Solution solver(pre,pos);
  solver.solve();
  return 0;
}

