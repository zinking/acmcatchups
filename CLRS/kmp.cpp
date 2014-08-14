#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> calc_pi( const string& ptn );
int kmp_find( const string& str, const string& ptn ){
  auto pi = calc_pi(ptn);
  int m = ptn.length();
  int q=-1;
  for( int i=0;i<str.length();i++){
    while( q>0 && ptn.at(q+1) != str.at(i) ) q = pi[q];
    if( ptn.at(q+1) == str.at(i) ) q++;
    if( q == m-1 ) return i-m+1;
  }
  return -1;
}

//some key points
//pi is move length not jump to index
//subptr always looks forward to seek for match
vector<int> calc_pi( const string& ptn ){
  int m = ptn.length();
  vector<int> pi( m,0 );
  int k=0;
  pi[0] = 0;
  for( int q=1;q<m;q++ ){
    while( k>0 && ptn.at(k+1) != ptn.at(q) ) k = pi[k];
    if( ptn.at(k+1) == ptn.at(q) ) k++;
    pi[q]=k;
  }
  //cout << "PTN done" << endl;
  return pi;
}


void TestCase( const string& str, const string& p, int expected ){
  static int caseno = 1;
  int actual = kmp_find( str, p );
  if( actual == expected ){
    cout << "CASE:"<< caseno << " PASS" << endl;
  }
  else{
    cout << "CASE:"<< caseno << " FAIL " ;
    cout << "Expected:"<< expected << " Actual:" << actual << endl;
  }
  caseno++;
}



int main(){
  TestCase( "cat", "dog" , -1 );
  TestCase( "a", "a" , 0  );
  TestCase( "cat", "cat" , 0  );
  TestCase( "dogcatcat", "catcat" , 3  );

  return 0;
}
