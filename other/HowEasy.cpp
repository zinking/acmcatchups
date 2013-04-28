#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <cctype>
#include <vector>

using namespace std;
class HowEasy{
public:
  int pointVal( string s ){
    vector<string> tokens;
    istringstream iss(s);
    copy( istream_iterator<string>(iss), istream_iterator<string>(),
	  back_inserter<vector<string> >(tokens));
    int nv = 0;
    int nvlength = 0;
    for( int i=0; i<tokens.size(); i++ ){
      string word = tokens[i];
      if( validWord( word ) ){
	nv++;
	int c=word[word.size() -1 ] == '.' ?-1:0; 
	nvlength += tokens[i].size()+c;
      }
    }

    if( nv == 0 ) return 250;
    int avg = nvlength / nv;
    if( avg <= 3 ) return 250;
    else if ( avg <=5 ) return 500;
    else return 1000;

  }

  int validWord( string tk ){
    if ( tk.size() == 1 && !isalpha(tk[0])) return 0;
    for( int j=0; j<tk.size(); j++ ){
      if( (j < tk.size()-1)  && (isalpha( tk.at(j) ) == 0) ) return 0;
      else if( (j == tk.size() -1) && ( isalpha( tk.at(j) ) || tk.at(j) == '.' ) ) return 1;
    }
  }

};

int main(){
  HowEasy h;
  cout << h.pointVal( "and. . and.") << endl;

  return 0;
}
