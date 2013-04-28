#include <iostream>
using namespace std;

char  B[4][4];

//inline void p( int xcount, int ocount, int tcount, int dcount )

void judge_status( int caseno ){
  //judge rows:
  int i=0,j=0;
  int xcount=0,ocount=0,tcount=0,dcount=0;

  for( i=0;i<4;i++){
    for( j=0;j<4;j++){
      cin >> B[i][j];
    }
  }
  for( i=0;i<4;i++){
    xcount=0,ocount=0,tcount=0;
    for( j=0;j<4;j++){
      switch( B[i][j] ){
      case 'X':
	xcount++;
	break;
      case 'T':
	tcount++;
	break;
      case 'O':
	ocount++;
	break;
      }
    }

    if( xcount==4 || ( xcount == 3 && tcount == 1 ) ){
      cout << "Case #" << caseno << ": " << "X won" << endl;
      return;
    }
    if( ocount==4 || ( ocount == 3 && tcount == 1 ) ){
      cout << "Case #" << caseno << ": " << "O won" << endl;
      return;
    }
  }

  
  for( j=0;j<4;j++){
    xcount=0,ocount=0,tcount=0;
    for( i=0;i<4;i++){
      switch( B[i][j] ){
      case 'X':
	xcount++;
	break;
      case 'T':
	tcount++;
	break;
      case 'O':
	ocount++;
	break;
      case '.':
	dcount++;
	break;
      }
    }

    if( xcount==4 || ( xcount == 3 && tcount == 1 ) ){
      cout << "Case #" << caseno << ": " << "X won" << endl;
      return;
    }
    if( ocount==4 || ( ocount == 3 && tcount == 1 ) ){
      cout << "Case #" << caseno << ": " << "O won" << endl;
      return;
    }
  }

  //left diagonal

  xcount=0,ocount=0,tcount=0;
  for( i=0;i<4;i++){
      switch( B[i][i] ){
      case 'X':
	xcount++;
	break;
      case 'T':
	tcount++;
	break;
      case 'O':
	ocount++;
	break;
      }
  }
  if( xcount==4 || ( xcount == 3 && tcount == 1 ) ){
    cout << "Case #" << caseno << ": " << "X won" << endl;
    return;
  }
  if( ocount==4 || ( ocount == 3 && tcount == 1 ) ){
    cout << "Case #" << caseno << ": " << "O won" << endl;
    return;
  }
  //right diagonal
  xcount=0,ocount=0,tcount=0;
  for( i=0;i<4;i++){
    switch( B[i][3-i] ){
    case 'X':
      xcount++;
      break;
    case 'T':
      tcount++;
      break;
    case 'O':
      ocount++;
      break;
    }
  }
  if( xcount==4 || ( xcount == 3 && tcount == 1 ) ){
    cout << "Case #" << caseno << ": " << "X won" << endl;
    return;
  }
  if( ocount==4 || ( ocount == 3 && tcount == 1 ) ){
    cout << "Case #" << caseno << ": " << "O won" << endl;
    return;
  }

  if( dcount > 0 ){
    cout << "Case #" << caseno << ": " << "Game has not completed" << endl;
    return;
  }
  else{
    cout << "Case #" << caseno << ": " << "Draw" << endl;
    return;
  }

}


void judge_bits(){
}

int main(){
  int T=0;
  cin >> T;
  for ( int i=0; i<T; i++ ){
    judge_status(i+1);
  }

  return 0;
}
