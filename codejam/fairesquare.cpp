#include <iostream>
#include <cmath>

using namespace std;
typedef unsigned long long ULONG;
bool isPal( ULONG num ){
  ULONG n = num;
  int digit = 0;
  ULONG rev = 0;
  while( num ){
    digit = num % 10;
    rev = rev * 10 + digit;
    num /= 10;
  }

  return n == rev;
}

void test_fair_square( int test ){
  ULONG s=0,e=0;
  cin >> s >> e;

  ULONG ss=(ULONG)sqrt(s)-1;
  ULONG ee=(ULONG)sqrt(e)+1;

  int count = 0;
  for( ULONG i=ss;i<ee; i++ ){
    ULONG nn = i*i;
    if ( !isPal(i)) continue;
    if ( nn < s || nn > e ) continue;
    if ( isPal( nn ) ) {
      count ++ ;
      //cout << "n:" << nn << endl;
    }
  }
  
  cout << "Case #" << test << ": " << count << endl;
}

int main(){
  int n=0;
  cin >> n;
  for( int i=0; i<n; i++ ){
    test_fair_square( i+1 );
  }

  return 0;
}



