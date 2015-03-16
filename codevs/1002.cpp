#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;


char M[50][50];
int  V[50][50];
int  C[2000];
int m=0,n=0,c=0,b=0;
//row count, col count, city count, bridge count;
int dir[8][2] = {
  {-1,0},
  {0,1},
  {1,0},
  {0,-1},
  {1,-1},
  {1,1},
  {-1,1},
  {-1,-1}
};


bool is_valid( int r, int c ){
  return (r>=0)&&(r<m)&&(c>=0)&&(c<n);
}

int findc( int c ){
  if( C[c]==c ) return c;
  return findc(C[c]);
  
}

void probe_bridge( int i, int j, int c ){
  //if bridge is even larger probably use convex to get wraping rectangel and then calculate

  //printf("Probe: %d,%d from: city:%d \n",i,j,c);
  for(int ii=0;ii<4;ii++){
    //WA result, probably need to figure out the distance between here and original
    int dr=dir[ii][0]+i;
    int dc=dir[ii][1]+j;
    if( is_valid(dr,dc)  ){
      int nc=V[dr][dc];
      if( nc == 0 ) continue;
      int cc=findc(nc);
      int oc=findc(c);
      //printf("!!!!: (%d,%d) ->(%d,%d) city:%d(%d) -> %d (%d) for bridge\n",i,j,dr,dc,c,oc,nc,cc);

      if( oc != cc ){
        //not connected to the bridged country
        ++b;
        C[cc]=C[oc]=min(cc,oc);
        
        //printf("Probe: %d,%d city:%d -> %d (%d) for bridge\n",i,j,c,nc,cc);
      }
    }
  }
}



void dfs( int i, int j, int c ){
  if( M[i][j] == '.' ) {
    probe_bridge( i,j,c);
    return;
  }
  if( V[i][j] > 0 ){
    //probe_bridge( i,j,c );
    return;
  }
  V[i][j] = c;
  for( int ii=0;ii<8;ii++){
    int dr=dir[ii][0]+i;
    int dc=dir[ii][1]+j;
    if( is_valid(dr,dc) ){
      dfs(dr,dc,c);
    }
  }
}

void process(){
  for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
      if(V[i][j]==0 && M[i][j]=='#') dfs(i,j,++c);
    }
  }
  cout << c << endl;
  cout << b << " " << b << endl;
}

int main(){
  cin >> m >> n;
  char ch='.';
  memset(M,0,sizeof(M));
  memset(V,0,sizeof(V));
  //memset(C,0,sizeof(C));
  for(int k=0;k<2000;k++) C[k]=k;
  for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
      cin >> ch;
      M[i][j]=ch;
    }
  }
  process();
  return 0;
}
