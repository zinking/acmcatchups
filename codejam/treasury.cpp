#include <iostream>
#include <cstring>

using namespace std;

const int MAX=201;

int ADJ[MAX][MAX]; //adjmatrix
int AHK[MAX][MAX]; //keys stored in the chest
int AK[MAX];//need AK[i] to open chest i
int NK[MAX];//need key
int HK[MAX];//has key


bool found_flag = false;

void BFS( int test, int* OK, int c, int cn, int n , int* v, bool* VV);

void find_treasure( int test ){
  int kn=0,n=0;
  cin >> kn >> n;
  //debug
  //cout << kn << " " << n << endl;
  int OK[MAX];//keys owned
  memset( OK, 0, sizeof( OK ) );

  memset( NK, 0, sizeof(NK) );
  memset( HK, 0, sizeof(HK) );


  int i=0,j=0,k=0;
  for( i=0; i<kn; i++ ){
    int st_key = 0;
    cin >> st_key;
    OK[st_key]++;
    HK[st_key]++;
  }

  found_flag = false;
  int  V[MAX];//record the visit sequence
  memset( V, 0, sizeof( V ) );
  bool  VV[MAX];//if chest is visited
  memset( VV, 0, sizeof( VV ) );


  //int AK[MAX];//need AK[i] to open chest i
  memset( AK, 0, sizeof( AK ) );

  //int A[MAX][MAX]; //adjmatrix
  //memset( ADJ, 0 , sizeof( ADJ ) );
  
  //int AHK[MAX][MAX]; //adjmatrix
  memset( AHK, 0 , sizeof( AHK ) ); 

  for ( i=0; i<n; i++ ){
    int ti=0,kin=0;
    int ki=0;

    cin >> ti >> kin;
    AK[i+1] = ti;
    NK[ti]++;
    for( j=0; j<kin; j++ ){
      cin >> ki;//chest i+1 has ki
      AHK[i+1][j] = ki;
      HK[ki]++;
    }
  }

  for( i=0; i<MAX; i++ ){
    if( HK[i] < NK[i] ){
      cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
      return;
    }
  }

  /*
  for( i=1; i<=n; i++ ){//look at the keys inside chest i
    for( j=0; AHK[i][j]!=0 ; j++ ){
      for( k=1; k<=n; k++ ){//build the adjmatrix
	if( AK[k]== AHK[i][j] ){
	  ADJ[i][k] = AHK[i][j]; // we can arrive at chest k using key AHK[j]
	}
      }
    }
  }
  

  
  for( i=1; i<=n; i++ ){
    for( j=1; j<=n; j++ ){
      cout << ADJ[i][j]<<" ";
    }
    cout << endl;
  }
  return;
 */
      

  for( j=1; j<=n; j++ ){
    if( OK[AK[j]] > 0 ){
      //OK[AK[j]]--;
      BFS( test, OK, j, 0, n , V , VV);
      //OK[AK[j]]++;
    }
  }
  if( !found_flag ) cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
}

void BFS( int test, int* OK, int c, int cn, int n , int* V, bool* VV){
  //testcase id, owned_keys, current node, visited count, total count, visit sq

  //debug
  /*
  {
    for( int ii=0; ii<= cn; ii++ )
      cout << V[ii] << " ";
    cout << endl;
    }
  */
  
  if( found_flag ) return;
  int i=0,j=0,k=0;
  OK[AK[c]]--;
  HK[AK[c]]--;
  V[cn] = c;
  VV[c] = true;
  if( cn == n-1 ){
    found_flag = true;
    cout << "Case #" << test << ": ";
    for( i=0; i<n; i++ ){
      cout << V[i] << " ";
    }
    cout << endl;
    return;
  }

  bool has_dead_node = false;
  
  for( j=0; AHK[c][j] != 0; j++ ){
    int ki = AHK[c][j];
    OK[ki]++;
    HK[ki]++;
  }

  for( j=1; j<=n; j++ ){
    if( !VV[j] ){//detect dead node
      int HHK[MAX];
      memcpy( HHK, HK, sizeof( HHK ));

      int ki = AK[j];
      for( i=0; AHK[j][i] != 0; i++ ){//take the keys the chest has out
	HHK[ AHK[j][i] ] --;
      }
      if( HHK[ki] == 0 ){
	has_dead_node = true;
	//cout << "dead node " << j << endl;
	break;
      }
      /*
      for( k=1; k<=n; k++ ){
	if ( !VV[k] && HHK[ AK[k] ] == 0 ){//if some nodes are unreachable then
	
	  for( int mm=0; mm<=cn; mm++ )
	    cout << V[mm] << " ";
	  cout << endl;
	  cout << "return because dead node " << k << endl;
	  
	  return;

	  has_dead_node = true;
	  break;
	}
	}*/
    }
  }

  if( !has_dead_node ){
    for( j=1; j<=n; j++ ){
      if( OK[AK[j]] > 0 && !VV[j] ){
	//OK[AK[j]]--;
	BFS( test, OK, j, cn+1, n , V , VV);
	//OK[AK[j]]++;
      }
    }
  }


  /*
  for( i=1;i<=n;i++ ){
    int ki = ADJ[c][i];
    if( ki != 0 && !VV[i] && ( OK[ki] > 0 ) ){
      OK[ki]--;
      BFS( test, OK, i, cn+1, n, V );
      OK[ki]++;
    }
    }
  */

    
  
  for( j=0; AHK[c][j] != 0; j++ ){
    int ki = AHK[c][j];
    OK[ki]--;
    HK[ki]--;
  }

  VV[c] = false;
  V[cn] = 0;
  HK[AK[c]]++;
  OK[AK[c]]++;
}

int main(){
  int n = 0;
  cin >> n;
  for( int i=0;i<n; i++ ){
    find_treasure( i+1 );
  }
}
    
