#include<iostream>

using namespace std;

bool ch_in_str( const char* ch, const char* h ){
  if( !(*h) ) return false;
  return( (ch!=h)&&(*ch==*h)) || ch_in_str( ch, h+1 );
}

void remove_duplicate( const char* str ){
  const char* p = str;
  while( *p ){
    if( !ch_in_str( p, p+1 ) ) cout << *p ;
    p++;
  }
}


int main(){
  cout << "1.remove duplicate in [FOLLOWUP] ";
  remove_duplicate( "FOLLOWUP" );
  cout << endl;
  cout << "2.remove duplicate in [FLLLOLLWFOWUP] ";
  remove_duplicate( "FLLLOLLWFOWUP" );
  cout << endl;
  return 0;
}
