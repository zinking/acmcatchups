#include <iostream>
#include <cmath>
#include <stack>
using namespace std;

struct nd{
  int d;
  nd* l;
  nd* r;
  nd* p;
  
  nd( int dd ){
    d = dd;
    l = r = p = NULL;
  }
};


struct btree{
  nd* root;

  btree():root(NULL){}
  
  void delete_nd( nd* n ){
    nd* t;
    if( !(n->l) || !(n->r) ){
      t = n;
    }
    else t=in_suc(n);
    nd* c;
    t->l ? c=t->l : c=t->r;
    if( c ) c->p = t->p;
    if( t == t->p->l ) t->p->l = c;
    else t->p->r = c;
    
    if( t!=n ) n->d = t->d;
    delete t;
  }
  
  void delete_nd1( nd* n ){
    nd* t = NULL;
    if( !n->l && !n->r ) t=n;
    else t=in_suc( n );
    nd* p = t->p;
    n->d = t->d;
    if( t == p->l ) {
      p->l = NULL;
      if( t->l ){
	t->l->p = t->p;
	p->l = t->l;
      }
      if( t->r ){
	t->r->p = t->p;
	p->l = t->r;
      }
    }

    if( t == p->r ){
      p->r = NULL;
      if( t->l ){
	t->l->p = t->p;
	p->r = t->l;
      }
      if( t->r ){
	t->r->p = t->p;
	p->r = t->r;
      }
    }
    delete t;
  }
  
  void in_output(nd* n ){
    if( n && n->l ) in_output( n->l );
    if( n ) cout << " " << n->d ;
    if( n && n->r ) in_output( n->r );
  }
		  

  bool isBST(nd* n){
    static int LV = -1;
    bool f = true;
    if( !f ) return false;
    if( n ){
      
      if(n->l) isBST(n->l);
      if( LV > n->d ) {
	//cout << " NOT BST " ;
	f = false;
	return false;
      }
      else{
	LV = n->d;
      }
      
      if( n->r) isBST(n->r);
    }
    return true;
  }

  int nonrecursive_height( nd* n ){
    int r=0;
    stack<nd*> v;
    v.push( n );
    while( !v.empty() ){
      nd* c=v.top();
      v.pop();
      if( c->l || c->r ){
	if( c->l ) v.push( c->l );
	if( c->r ) v.push( c->r );
      }
      else{
	nd* p=c;
	int rr=0;
	do{
	  rr++;
	  p=p->p;
	}while( p&&c!=n );
	r=max(rr,r);
      }
    }
    return r;
  }

  void insert_at( nd* n, nd** at, nd* p ){
    if( !(*at) ){
      *at = n;
      n->p = p;
    }
    else if( n->d < (*at)->d ){
      insert_at( n, &((*at)->l), *at );
    }
    else if( n->d >= (*at)->d ){
      insert_at( n, &((*at)->r), *at );
    }
    return;
  }

  nd* leftmost( nd* n ){
    nd* r = n;
    while( r && r->l ) r=r->l;
    return r;
  }

  nd* rightmost( nd* n ){
    nd* r = n;
    while( r && r->r ) r= r->r;
    return r;
  }

  nd* in_suc( nd* n ){
    if( n && n->r ) return leftmost( n->r );
    nd* p = n->p;
    while( n == p->r ){
      n = p;
      p = n->p;
    }
    return p;
  }

  nd* in_pre( nd* n ){
    if( n && n->l ) return rightmost( n->l );
    nd* p = n->p;
    while( n == p->l ){
      n=p;
      p=n->p;
    }
    return p;
  }
};


int main(){
  btree b;
  b.insert_at( new nd(15), &b.root, NULL );
  nd* z3 = new nd( 5 );
  b.insert_at( z3, &b.root, NULL );
  nd* z2 = new nd( 16 );
  b.insert_at( z2, &b.root, NULL );
  b.insert_at( new nd(3), &b.root, NULL );
  b.insert_at( new nd(12), &b.root, NULL );
  b.insert_at( new nd(20), &b.root, NULL );
  b.insert_at( new nd(10), &b.root, NULL );
  nd* z1 = new nd(13);
  b.insert_at( z1, &b.root, NULL );
  b.insert_at( new nd(18), &b.root, NULL );
  b.insert_at( new nd(23), &b.root, NULL );
  b.insert_at( new nd(6), &b.root, NULL );
  b.insert_at( new nd(7), &b.root, NULL );
  
  b.in_output( b.root );
  cout << endl;
  cout << "B's height " << b.nonrecursive_height( b.root ) << endl;

  b.delete_nd( z1 );
  b.in_output( b.root );
  cout << endl;
  
  b.delete_nd(z2);
  b.in_output( b.root );
  cout << endl;
  
  b.delete_nd(z3);
  b.in_output( b.root );
  cout << endl;
  cout << "B IS BSTREE ? " << b.isBST( b.root ) << endl;

  btree b2;
  b2.insert_at( new nd(10), &b2.root, NULL );
  b2.insert_at( new nd(15), &(b2.root->l), b2.root );
  b2.insert_at( new nd(6),  &(b2.root->r), b2.root );

  cout << "B2 IS BSTREE ? " << b2.isBST( b2.root ) << endl;
  return 0;
 
}
