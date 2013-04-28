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

  /*
  BigNumber( const BigNumber& r ){
    memcpy( digits,r.digits, sizeof(digits));
  }
  */
  

  BigNumber(){
    memset( digits, 0, sizeof(digits));
  }

  BigNumber Add( BigNumber r ){
    BigNumber c;
    int i=0;
    for( i=0; i<MD; i++ ){
      c.digits[i] = digits[i] + r.digits[i];
    }
    for( i=0; i<MD; i++ ){
      c.digits[i+1] = c.digits[i]/10;
      c.digits[i] %= 10;
    }
    return c;
  }

  BigNumber Sub( BigNumber r ){
    BigNumber c;
    int i=0;
    for( i=0; i<MD; i++ ){
      c.digits[i] = digits[i]-r.digits[i];
    }
    for( i=0; i<MD; i++ ){
      if( c.digits[i] < 0 ){
	c.digits[i+1]--;
	c.digits[i]+=10;
      }
    }
    return c;
  }

  BigNumber Mul( int d ){
    BigNumber c;
    int i=0;
    for( i=0; i<MD; i++ ){
      c.digits[i] = digits[i]*d;
    }
    for( i=0; i<MD; i++ ){
      c.digits[i+1] = c.digits[i]/10;
      c.digits[i] %= 10;
    }

    return c;
  }

  BigNumber Add( int d ){
    BigNumber c(*this);
    int i=0;
    c.digits[0]+=d;
    for( i=0; i<MD; i++ ){
      c.digits[i+1] = c.digits[i]/10;
      c.digits[i]%=10;
    }
    return c;
  }

  int nd()const{
    int i=0,nd=0;
    for( int i=MD-1;i>=0;i--){
      if( digits[i] != 0 ){
	nd = i+1;
	break;
      }
    }
    return nd;
  }

  int cmp( BigNumber r ){
    int nnd=0,rnd=0,i=0;
    nnd = this->nd();
    rnd = r.nd();
    if ( nnd != rnd ){
      return nnd - rnd;
    }
    else{
      int i=0;
      for( i=0; i<nnd;i++ ){
	if( digits[i] == r.digits[i] ) continue;
	else{
	  return digits[i] - r.digits[i];
	}
      }
      return 0;
    }
  }

  BigNumber sqrt( ){
    int i=0,x=0,nnd=0;
    BigNumber p,c,y;
    nnd = this->nd();
    int pn = (nnd+1)/2;
    //BigNumber c,y;
    //BigNumber p;

    for( i=pn-1; i>=0; i-- ){
      //c = c*100 + digits[(2*i+1)]*10+digits[(2*i)];
      //for( x=0; x*(20*p+x)<=c; ++x);
      c = c.Mul(100).Add( digits[(2*i+1)]*10+digits[(2*i)] );
      while( y.cmp(c)<=0 ){
	//y=x*(20*p+x);
	x++;
	y=(p.Mul(20).Add(x)).Mul(x);
      }
      //c -= y;
      x--;
      y=(p.Mul(20).Add(x)).Mul(x);
      c = c.Sub(y);
      //p = p*10 + x;
      p = p.Mul(10).Add(x);
    }

    return p;
  }
  
  friend ostream& operator<<(ostream& out, const BigNumber& b );
};

ostream& operator<<(ostream& out, const BigNumber& b){
  int nd = b.nd();
  for( int i=nd-1; i>=0; i-- ){
     out << b.digits[i];
  }
  return out;
}



int main( ){
  BigNumber l("1024");
  cout << l.Mul(100).Add(11) << endl;
  //cout << l << " sqrt:" << l.sqrt() << endl;
  //cout << "0 sqrt " << r.sqrt() << endl;
  return 0;
}
