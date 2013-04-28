#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

const int MD = 10;
struct BigNumber{
  int digits[MD];
  BigNumber( const char* p ){
    memset( digits, 0, sizeof(digits));
    int plen = strlen( p );
    for( int i=plen-1; i>=0; i-- ){
      digits[plen-1-i]=p[i]-'0';
    }
  }

  BigNumber(){
    memset( digits, 0, sizeof(digits));
  }

  BigNumber test(){
    BigNumber p,c,y;
    p=c;
    c=y;
    //y=p;
    return y;
  }
      

  friend ostream& operator<<(ostream& out, const BigNumber& b );
};

ostream& operator<<(ostream& out, const BigNumber& b){
  for( int i=MD-1; i>=0; i-- ){
     out << b.digits[i];
  }
  return out;
}



int main( ){
  BigNumber l("4");
  BigNumber r;
  BigNumber p,c,y;

  r=l.test();
  cout << r << endl;
  cout << l.test() << endl;
  return 0;
}
