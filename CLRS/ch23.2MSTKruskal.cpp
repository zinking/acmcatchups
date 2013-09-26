#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

struct el{
  int fm;
  int to;
  int w;
  el* n;
  el( int ff, int tt, int ww ):fm(ff),to(tt),w(ww),n(NULL){}
};

const int M=10;
int p[M];

int find( int x ){
  return x==p[x] ? x:p[x]=find( p[x] );
}

void union_set( int x, int y ){
  p[find(x)] = y;
}

bool sameset( int x, int y ){
  return find(x) == find(y);
}

bool comp_e( el* l, el* r ){
  return ( l->w ) < ( r->w );
}

struct Graph{
  el* v[M];
  Graph(){
    memset(v,0,sizeof(v));
  }

  ~Graph(){
    for( int i=0; i<M; i++ ) freev( v[i] );
  }

  void freev( el* h ){
    while( h ){
      el* c = h;
      h=h->n;
      delete c;
    }
  }


  void add_edge( int i, el* e ){
    el* c=v[i];
    if( !c ) v[i] = e;
    else{
      while( c->n ) c=c->n;
      c->n = e;
    }
  }

  
  void MST_Kruskal(){
    vector<el*> edges;
    for( int i=0; i<M; i++ ){
      p[i] = i;
      el* h = v[i];
      while( h ) {
	edges.push_back( h );
	h=h->n;
      }
    }
    
    sort( edges.begin(), edges.end(), comp_e );

    vector<el*> r;
    int n = edges.size();
    for( int i=0; i<n; i++ ){
      el* e = edges[i];
      if( !sameset( e->fm, e->to ) ){
	union_set( e->fm, e->to );
	r.push_back(e);
      }
    }

    cout << "edges in MST" << endl;
    n = r.size();
    for( int i=0; i<n; i++ ){
      el* e = r[i];
      cout << e->fm << " -> " << e->to << " " << e->w << endl;
    }
  }
  
  void MST_Prim( int n ){
    static int w[M];
    static bool vs[M];
    static int p[M];
    for( int i=0; i<n; i++ ){
      w[i]=0xefff;
      vs[i]=false;
      p[i]=0;
    }

    vs[0] = true;
    w[0] = 0;
    int vi=0;
    
    while ( vi != -1 ){
      el* e = v[vi];
      int mw = 0xefff;
      while( e  ){
	if( !vs[e->to] && ( w[e->to] > (e->w)) ){
	  w[e->to] = e->w;
	  p[e->to] = e->fm;
	}
	e = e->n;
      }
      vi = extract_min( w,vs,n );
    }
    
    for( int i=1; i<n; i++ ){
      cout << p[i] << " -> " << i << " " << w[i] << endl;
    }
  }
  
  int extract_min( int* w, bool* vs, int n ){
    int mw = 0xefff;
    int vi = -1;
    for( int i=0; i<n; i++ ){
      if( !vs[i]  && w[i] < mw ){
	vi = i;
	mw = w[i];
      }
    }
    vs[vi] = true;
    return vi;
  }
      
};


int main(){
  Graph g;
  g.add_edge( 0, new el( 0,1,4 ) );
  g.add_edge( 0, new el( 0,2,8 ) );
  g.add_edge( 1, new el( 1,2,11) );

  g.MST_Kruskal();
  
  cout << "CLRS sample" << endl;

  Graph g1;
  g1.add_edge( 0, new el( 0,1,4) );
  g1.add_edge( 0, new el( 0,7,8) );
  g1.add_edge( 1, new el( 1,7,11) );
  g1.add_edge( 1, new el( 1,2,8) );
  g1.add_edge( 2, new el( 2,8,2) );
  g1.add_edge( 7, new el( 7,8,7) );
  g1.add_edge( 2, new el( 2,3,7) );
  g1.add_edge( 2, new el( 2,5,4) );
  g1.add_edge( 6, new el( 6,8,6) );
  g1.add_edge( 6, new el( 6,7,1) );
  g1.add_edge( 6, new el( 6,5,2) );
  g1.add_edge( 3, new el( 3,5,14) );
  g1.add_edge( 3, new el( 3,4,9) );
  g1.add_edge( 4, new el( 4,5,10) );
 
  g1.MST_Kruskal();
  
  cout << "PRIM sample " << endl;
  
    Graph g2;
  g2.add_edge( 0, new el( 0,1,4) );
  g2.add_edge( 1, new el( 1,0,4) );

  g2.add_edge( 0, new el( 0,7,8) );
  g2.add_edge( 7, new el( 7,0,8) );

  g2.add_edge( 1, new el( 1,7,11) );
  g2.add_edge( 7, new el( 7,1,11) );

  g2.add_edge( 1, new el( 1,2,8) );
  g2.add_edge( 2, new el( 2,1,8) );

  g2.add_edge( 2, new el( 2,8,2) );
  g2.add_edge( 8, new el( 8,2,2) );

  g2.add_edge( 7, new el( 7,8,7) );
  g2.add_edge( 8, new el( 8,7,7) );

  g2.add_edge( 2, new el( 2,3,7) );
  g2.add_edge( 3, new el( 3,2,7) );

  g2.add_edge( 2, new el( 2,5,4) );
  g2.add_edge( 5, new el( 5,2,4) );

  g2.add_edge( 6, new el( 6,8,6) );
  g2.add_edge( 8, new el( 8,6,6) );

  g2.add_edge( 6, new el( 6,7,1) );
  g2.add_edge( 7, new el( 7,6,1) );

  g2.add_edge( 6, new el( 6,5,2) );
  g2.add_edge( 5, new el( 5,6,2) );

  g2.add_edge( 3, new el( 3,5,14) );
  g2.add_edge( 5, new el( 5,3,14) );

  g2.add_edge( 3, new el( 3,4,9) );
  g2.add_edge( 4, new el( 4,3,9) );

  g2.add_edge( 4, new el( 4,5,10) );
  g2.add_edge( 5, new el( 5,4,10) );
  
  g2.MST_Prim(9);
  

  return 0;
}


