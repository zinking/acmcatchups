#include <iostream>
using namespace std;

struct nd{
  int d;
  nd* n;
  nd( int n ){
    d = n;
    this->n = NULL;
  }
};


nd* make_number( int n ){
  nd* h=new nd(0);
  nd* l=h;
  while( n ){
    l->d=n%10;
    n/=10;
    if( n ){
      l->n=new nd(0);
      l=l->n;
    }
  }
  return h;
}

void free_number( nd* h ){
  while( h ){
    nd* c = h;
    h = h->n;
    delete c;
  }
}


nd* add_number( nd* n1, nd* n2 ){
  nd* h = new nd(0);
  nd* l = h;
  int c = 0;
  while( n1 || n2 ){
    int d1 = n1 ? n1->d:0;
    int d2 = n2 ? n2->d:0;
    int s = d1+d2+c;
    l->d = s%10;
    c = s/10;

    if( n1 ) n1=n1->n;
    if( n2 ) n2=n2->n;
    if( n1|| n2){
      l->n = new nd(0);
      l = l->n;
    }
  }
  return h;
}

void print_number( nd* h ){
  if( !h ) return ;
  print_number( h->n);
  cout << h->d;
}

nd* rhead = NULL;

nd* reverse_nd( nd* h){//this logic is incorrect, not fixing the ohead->next 
  if( h && !(h->n) ) {
    rhead = h;
    return h;
  }
  //if( !h ) return NULL;
  nd* n = reverse_nd( h->n );
  if( n ) n->n = h;
  return h;
}


int main(){
  nd* n1 = make_number( 1995 );
  nd* n2 = make_number( 29983 );
  nd* s  = add_number( n1, n2 );
  print_number( s );
  cout << " Expected: " << 1995+29983 << endl;

  reverse_nd( n2 );
  n2->n = NULL;
  print_number(rhead );
  cout << endl;
  
  free_number( n1 );
  free_number( n2 );
  free_number( s  );
  return 0 ;
}
    
