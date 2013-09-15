#include<iostream>
using namespace std;

int add( int a, int b){
  if( b==0 ) return a;
  int x = a^b;
  int c = a&b;
  return add(x,c<<1);
}


int main(){
  cout << "add use bit operator tests" << endl;
  cout << "1+1="     << add(1,1)        << endl;
  cout << "100+111=" << add(100,111)    << endl;

  cout << "2+(-1)="  << add(2,-1)       << endl;
  cout << "-1+(-1)=" << add(-1,-1)      << endl;

  return 0;
}
