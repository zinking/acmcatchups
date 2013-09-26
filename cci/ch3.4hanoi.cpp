#include<cstdio>
#include<cstdlib>

#include<stack>
using namespace std;


void Hanoi_move( int tower, int cnt, int from, int to ){
  if( cnt == 1 ){
    printf( "move %d : %d -> %d \n", tower, from , to );
    return;
  }
  else{
    int extra = 3 - from - to ;
    Hanoi_move( tower-1, cnt-1, from , extra );
    Hanoi_move( tower,   1    , from , to    );
    Hanoi_move( tower-1, cnt-1, extra, to    );
  }
}

struct Hn{
  int tower;
  int cnt;
  int from;
  int to;
  Hn( int t, int c, int fm, int to ):tower(t),cnt(c),from(fm),to(to){}
};

void Hanoi( stack<Hn>& s ){
  while( !s.empty() ){
    Hn c = s.top();
    s.pop();
    if( c.cnt == 1 ){
      printf( "move %d: %d -> %d \n", c.tower, c.from, c.to );
    }
    else{
      int extra = 3 - c.from - c.to ;
      s.push( Hn( c.tower-1, c.cnt-1, extra, c.to ) );
      s.push( Hn( c.tower, 1,c.from, c.to ) );
      s.push( Hn( c.tower-1, c.cnt-1, c.from, extra));
    }
  }
}


int main(){
  //Hanoi_move( 3, 3, 0, 2 );
  stack<Hn> ss;
  ss.push( Hn( 3,3,0,2) );
  Hanoi( ss );

  return 0;
}
