#include <iostream>
using namespace std;

struct hn{
  int k;
  int v;
  hn* n;
  hn( int kk, int vv):k(kk),v(vv),n(NULL){}
};

  const int M=256;
class HashMap{
  hn* S[M];


  void free_hn( hn* h ){
    while( h ){
      hn* c = h;
      h = h->n;
      delete c;
    }
  }

  int hash_func( int key ){
    int p = 1037;
    int a = 100;
    int b = 1501;
    return ( (a*key+b)%p )%M;
  }

public:
  HashMap(){
    for( int i=0;i<M; i++ ) S[i]=NULL;
  }
  ~HashMap(){
    for( int i=0;i<M; i++ ) free_hn( S[i] );
  }
  
  void put( int k, int v ){
    hn* h = gethn( k );
    if( h ){
      h->v = v;
    }
    else{
      int slot = hash_func(k);
      hn* h=S[slot];
      while( h ) h=h->n;
      if( h ==  S[slot] ) S[slot] = new hn(k,v);
      else h = new hn(k,v);
    }
  }
  

  hn* gethn( int k ){//get current hnode with key k
    hn* h=S[hash_func(k)];
    while( h && h->k != k ) h=h->n;
    return h;
  }
  
  hn** getphn( int k ){//get previous node with key k
    int slot = hash_func(k);
    hn** p = &S[slot];
    if( (*p)->k == k ) return p;
    else{
      while( ( (*p)->n ) && (*p)->n->k != k ) p = &( (*p)->n );
    }
    return p;
  }

  int get( int k ){
    hn* h = gethn( k );
    return h?h->v:-1;
  }

  void erase_x2( int k ){
    hn** p = getphn( k );
    if( *p ){
      hn* c = *p;
      (*p)->n = c->n;
      delete c;
    }
  }

  void erase( int k ){
    if( !gethn(k) ) return;
    int slot=hash_func(k);
    hn* h = S[slot];
    hn* p = h;
    if( h->k == k ){
      S[slot] = p->n;
      delete p;
    }
    else{
      h = h->n;
      while( h && h->k != k ){
	p = p->n;
	h = h->n;
      }
      if( h ){
	p->n = h->n;
	delete h;
      }
    }
  }
};


int main(){
  HashMap m;
  m.put( 3,10);
  m.put( 3,15);
  m.put( 4,20);
  m.put( 5,21);

  cout << m.get(3) << endl;
  cout << m.get(4) << endl;
  m.erase( 3 );
  cout << m.get(3) << endl;

  return 0;
}
    

    
