#include<iostream>
#include<complex>
#include<valarray>
#include<cmath>
#include<algorithm>

using namespace std;


typedef complex<double> C;
typedef valarray<C> Ar;

const double PI = 3.14159265358979323846;
const double EPSILON = 0.000000001;


void fft( Ar& s ){
  int n = s.size();
  if( n<=1 ) return;
  
  Ar odd = s[ slice(1,n/2,2) ];
  Ar evn = s[ slice(0,n/2,2) ];
  
  fft(odd);
  fft(evn);

  for( int k=0; k<n/2; k++ ){
    C t = polar( 1.0, 2*k*PI/n ) * odd[k];
    s[k+0]   = evn[k]+t; 
    s[k+n/2] = evn[k]-t; 
    //although this looks odd and evn get mixed together
    //it is because the nature of valarray, it is still of length N instead of N/2
    //the negative is understood as W(N,N/2)=-1
  }

};

// consider fft as a matrix multiplication
// then ifft is the reverse of a vandermont matrix
// so the inverse is mathematically proved
void ifft( Ar& s ){
  int n=s.size();
  s=s.apply( conj ); 
  // c = p * M^-1 . where M is vandermont matrix
  // as Mn(w)^-1 = 1/n*Mn(w^-1)
  // this w^-1 could be separated into w(n,n/2) and w. the former could be extracted and applied on p as conjugate
  // TBP

  fft(s);
  s=s.apply( conj ); //this conjugation means nothing as we are using real part. to be confirmed
  s/=n;
}

void mul( Ar& l, Ar& r ){
  int nl=l.size(), nr=r.size(), n=1;
  while( n<(nl+nr) ) n<<=1;
  Ar ll( C(0), n );
  Ar rr( C(0), n );
  
  for( int i=0; i<nl; i++ ) ll[i] = l[i];
  for( int i=0; i<nr; i++ ) rr[i] = r[i];

  fft( ll );
  fft( rr );

  Ar cc = ll * rr ;
  ifft( cc );

  nr = cc.size();

  while( --nr >= 0  ){
    double v = cc[nr].real();
    if( abs(v-0) > EPSILON ) 
      cout << v << " ";
  }
  cout << endl;
}


int main(){
  // 7x^2 + 3x + 9
  // -13x + 5

  C ar1[3] = { 9, 3, 7 };
  C ar2[2] = { 5, -13 };

  Ar arr1( ar1,3 );
  Ar arr2( ar2,2 );
  mul( arr1, arr2 );

  return 0;
}
    
