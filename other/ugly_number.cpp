#include <iostream>

using namespace std;

int bfind( int a[], int l, int r, int num ){
  while( l <= r ){
    int m = ( l+r )/2;
    if( a[m] == num ) return m;
    else if ( a[m] < num ){
      l = m+1;
    }
    else if ( a[m] > num ){
      r = m-1;
    }
  }
  return -1;
}

void insert( int a[], int i, int num ){
  int j=i;
  while( a[j]>num && j>=0 ){
    a[j+1] = a[j];
    j--;
  }
  a[j+1]=num;
}

void uglynumber( const int m ){
  int N = 10000;
  int b[N] ;
  b[0] = 1;
  int mm = 1;

  int i;
  for( i=0; i<mm; i++ ){
    if( m == mm ) break;
    if( bfind(b,0,mm-1,b[i]*2 ) == -1  ){
      insert( b, mm-1, b[i]*2 );
      mm++;
    }

    if( m == mm ) break;
    if( bfind(b,0,mm-1,b[i]*3 ) == -1  ){
      insert( b, mm-1, b[i]*3 );
      mm++;
    }

    if( m == mm ) break;
    if( bfind(b,0,mm-1,b[i]*5 ) == -1  ){
      insert( b, mm-1, b[i]*5 );
      mm++;
    }

    if( m == mm ) break;
  }
  for( i=0; i<m; i++ ) cout << b[i] << " " ;
  cout << endl;
 
}


int main(){
  uglynumber( 8 );
  return 0;
}
