#include <iostream>
#include <cstring>

using namespace std;

void carry_operations( int* a, int* b){
  int c[10];
  memset(c,0,sizeof(c));
  int i=0;
  for( i=0; i<10; i++ ){
    c[i] = a[i] + b[i];
  }

  int carry_op = 0;
  for( i=0; i<10; i++ ){
    int e = c[i]/10;
    int d = c[i]%10;

    if( e > 0 ){
      c[i+1] += e;
      c[i] = d;
      carry_op++;
    }
  }

  if( carry_op > 0 ){
    if( carry_op > 1 ){
      cout << carry_op << " carry operations." << endl;
    }
    else{
      cout << "1 carry operation." << endl;
    }
  }
  else{
    cout << "No carry operation." << endl;
  }
}

int main(){
  int a[10],b[10];
  char aa[10],bb[10];
  int alen=0,blen=0;
  bool end=false;
  do{
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(a));

    alen=0;
    blen=0;

    cin >> aa >> bb;

    alen = strlen(aa);
    blen = strlen(bb);

    int i=0;
    for( i=alen-1;i>=0; i-- ){
      a[alen-1-i]=aa[i]-'0';
    }
    for( i=blen-1;i>=0; i-- ){
      b[blen-1-i]=bb[i]-'0';
    }

    end = (alen==1 && blen==1 && aa[0] == '0' && bb[0] == '0');
    if( !end ) carry_operations( a, b );
    else
      break;

  }while( true );

  return 0;

}
