#include<iostream>

using namespace std;

struct nd{
  char c;
  nd*  n;
  nd( char cc ):c(cc),n(NULL){}
};


nd* detect_loop( nd* h ){
  nd* n1=h;
  nd* n2=h;
  int d1=0;
  while( n2->n ){
    n1=n1->n;
    n2=n2->n->n;
    d1++;
    if( n1==n2 ) break;
  }

  if( !(n2->n) ) return NULL;

  int d2=0;
  n2 = h;

  while( true ){
    n1=n1->n;
    n2=n2->n;
    d2++;
    if( n1==n2 ) break;
  }

  return n1;
}


int main(){
  nd* h = new nd('a');
  nd* l = h;
  l->n  = new nd('b'); l=l->n;
  l->n  = new nd('c'); 
  l->n->n = l;

  nd* r = detect_loop( h );
  cout << r->c << endl;
  

  h = new nd('a');
  l = h;
  l->n = new nd('b'); l=l->n;
  l->n = new nd('c'); l=l->n;
  l->n = new nd('d'); l=l->n;
  l->n = new nd('e'); 
  l->n->n = l;
  r = detect_loop( h );
  cout << r->c << endl;

  
  return 0;
}
