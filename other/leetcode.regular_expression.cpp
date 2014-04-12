#include<iostream>
#include<cstring>
#include<cstdlib>
#include <cctype>

using namespace std;

const char* empty = "\1";

struct state{
  char ch;
  state* n[2];
  char f; //recording the state info
  char e;
  
  state( char c ):ch(c),f('c'),e('c'){
    memset( n, 0, sizeof( n ) );
  }
  
  bool pass(){
    if( f == '*' ){
      if( n[1] ) return n[1]->pass();
      else return true;
    }
    return false;
  }
  
};

state* parse_re( const char* pt ){
  if( *pt == '*' ) return 0;
  state *s, *n, *p;
  s = new state( *pt );
  p = s;
  pt++;
  while( *pt ){
    if( *pt == '*' ){
      p->n[0] = p;
      p->f = '*';
      const char* pp;
      for(  pp=pt+1; *pp!='\0';++pp){
	if( *pp!=p->ch ) break;
      }
      pt=pp-1;
    }
    else{
      //n = ( p->n[0] ? p->n[1]: p->n[0] );
      //n = new state( *pt );
      //p = n;
      if( !p->n[0] ){
	p->n[0] = new state( *pt );
	p=p->n[0];
      }
      else if( !p->n[1] ){
	p->n[1] = new state( *pt );
	p=p->n[1];
      }
    }
    pt++;
  }
  p->e = '$';
  return s;
}


bool match( const char* s, const state* p ){
  //if( *(s) == '\0' ){
  //  //if( !p->n[0] && !p->n[1] ) return true;
  //  //return false;
  //  return true;
  //}
  //if( p->ch == *s && *(s+1) == '\0' ) return true;
  
  //if( *s == '\0' ){
  //  if( !p ) return true;
  //  else if( p->end ) return true;
  //}


  
  bool path1=false, path2=false;
  bool matching = ( p->ch == '.' && isalpha(*s) ) || p->ch == *s ;
  
  if( *(s+1) == '\0' ){
    if( matching  && p->e == '$' ) return true;
    if( matching ){//p not reaching the end 
      //if( p->n[0] && p->n[0]->pass() && p->n[1] && p->n[1]->pass() ) return true;
      //else return false;
      bool p1 = true , p2 = true;
      if( p->n[0] ) p1 = p->n[0]->pass();
      if( p->n[1] ) p2 = p->n[1]->pass();
      if( p1&&p2 ) return true;
      else return false;
    }
  }
  //if( matching && *(s+1) == '\0' && p->end ) return true;
  //if( *s == '\0' && (p->n[0]==p ) ) return true;
  if( matching && p->n[0] ) path1 = match( s+1, p->n[0] );
  if( !path1 && p->n[1] ) path2 = match( s, p->n[1] );
  

  return path1 || path2 ;
}



class Solution{
public:
  bool isMatch( const char* s, const char* p ){
    state* nfs = parse_re( p );
    if( !nfs ) return false;
    return match( s, nfs );
  }
};

int main(){
  Solution s;
  cout << "Acutal\t\t" << "Expected\t\t" << endl;
  cout << s.isMatch( "aaa", "a*a") << true << endl;
  cout << s.isMatch( "ab", ".*c") << false << endl;
  cout << s.isMatch( "a", "ab*") << true << endl;
  cout << s.isMatch( "ab",".*c" ) << false << endl;
  cout << s.isMatch( "aa","a" ) << false << endl;
  cout << s.isMatch( "aa", "aa" ) << true << endl;
  cout << s.isMatch( "aaa", "aa" ) << false << endl;
  cout << s.isMatch( "aa", "a*") << true << endl;
  cout << s.isMatch( "aa", ".*") << true << endl;
  cout << s.isMatch( "ab", ".*") << true << endl;
  cout << s.isMatch( "aab", "c*a*b") << true << endl;
  return 0;

}
