#include<cmath>
#include<iostream>

using namespace std;

int neg( int x ){
  int s=x, r=0;
  int u=x>0?-1:1;
  while( s ){
    r+=u;
    s+=u;
  }

  return r;
}

int sub( int a, int b ){
  return a + neg(b);
}

int mul( int a, int b ){
  int an = abs(a);
  int r=0;
  for( int i=0; i<an; i++) r+=b;
  return a>0?r:neg(r);
}


int div( int a, int b){
  int aa=abs(a);
  int bb=abs(b);
  int i=1;
  for(;mul(bb,i)<aa;i++);
  if( (a>0&&b<0)||(a<0&&b>0)) return neg(i);
  return i;
}


int main(){
  cout << "arithmetic using add tests" << endl;
  cout << "  -5=" << neg(5)    << endl;
  cout << " 5-4=" << sub(5,4)  << endl;
  cout << "-5-4=" << sub(-5,4) << endl;
  cout << "-5*4=" << mul(-5,4) << endl;
  cout << "5*-4=" << mul(5,-4) << endl;
  cout << "-4/1=" << div(-4,1) << endl;
  return 0;
}

  
