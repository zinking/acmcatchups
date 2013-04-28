#include<iostream>
#include<cstring>
using namespace std;


int L[100][100];
int H[100];


//brutal force cut 100 times
int cut( int height , int m, int n){
  int i=0,j=0,count=0;
  int C[100][100];
  memset( C, 0, sizeof(C) );
  for( i=0;i<m; i++ ){
    int rcount = 0;
    bool mowed = true;
    for( j=0; j<n; j++ ){//test if the row is mownable
      if( L[i][j] > height ) {
	mowed = false;
	break;
      }
    }

    if ( mowed ){
      for( j=0; j<n; j++ ){
	if( (L[i][j] == height) && C[i][j]==0 ){
	  rcount++;
	  C[i][j] = 1;
	}
      }
    }
    count += rcount;
  }

  for( j=0; j<n; j++ ){
    int ccount = 0;
    bool mowed = true;
    for( i=0; i<m; i++ ){
      if( L[i][j] > height ) {
	mowed = false;
	break;
      }
    }
    if (mowed ){
      for( i=0; i<m; i++ ){
	if( (L[i][j] == height ) && C[i][j]==0 ){
	  ccount++;
	  C[i][j]=1;
	}
      }
    }
    count += ccount;
  }
  return count;
}

void test_cut( int test ){
  int m=0,n=0,i=0,j=0;
  memset( H, 0,sizeof(H) );
  cin >> m >> n;
  for( i=0; i<m; i++ ){
    for( j=0; j<n; j++ ){
      cin >> L[i][j];
      H[L[i][j]-1]++;
      //cout << L[i][j] << " ";
    }
    //cout << endl;
  }

  for( j=99; j>=0; j-- ){
    if ( H[j] == 0 ) continue;
    int mowed = cut( j+1, m, n );
    //cout << "mowing lawn at height:" << j+1 << " number:" << mowed << endl;
    if ( mowed < H[j] ){
      cout << "Case #"<< test << ": " << "NO" << endl;
      return;
    }
  }
  
  cout << "Case #"<< test << ": " << "YES" << endl;
}   

int main(){
  int n =0;
  cin >> n ;
  for( int i=0; i<n; i++ ){
    test_cut( i+1 );
  }
  return 0;
}

  
  
