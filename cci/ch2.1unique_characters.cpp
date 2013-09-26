#include<iostream>
#include<cstdlib>
#include<cstring>


using namespace std;

bool uch( const char* str ){
  int cnt[256];
  //memset( cnt, sizeof(cnt), 0 );
  memset( cnt, 0, sizeof(cnt));
  //char* p = str;
  //while( str ){
  while( *str ){
    //int k = ( int )(*p);
    int k = ( int )(*str);
    cnt[k]++;
    if( cnt[k] > 1 ) return false;
    str++;
  }
  return true;
}



int main(){
  cout << "unique characters [aa]:" << uch("aa") << endl;
  cout << "unique characters [aA]:" << uch("aA") << endl;
  cout << "unique characters [a1]:" << uch("a1") << endl;
  return 0;
}
