#include<cstdio>
#include<cstdlib>
#include<iterator>
#include<vector>
#include<cmath>
#include<set>
#include<algorithm>

using namespace std;

enum EPType{ Left,Right};
struct Vec2{
  int x;
  int y;
  Vec2( int xx,int yy):x(xx),y(yy){}
  
  Vec2 operator-(const Vec2& rhs )const{
    return Vec2(x-rhs.x,y-rhs.y);
  }
  
  int cross(const Vec2& rhs ){
    //x1 x2
    //y1 y2
    return x*rhs.y - rhs.x*y;
  }
  
  bool operator==(const Vec2& rhs )const{
    return x==rhs.x && y==rhs.y;
  }
  
  static bool isLeftUp( const Vec2& l, const Vec2& r ){
    return ( l.x <= r.x ) && ( l.y >= r.y );
  }

};

struct Segment{
  const Vec2* l;
  const Vec2* r;
  Segment(const Vec2&ll, const Vec2& rr):l(&ll),r(&rr){}
  
  bool Intersect( const Segment& rhs )const{
    return intersection( *l,*r, *(rhs.l), *(rhs.r) );
  }
  //s1 above s2
  static bool Above( const Segment* s1, const Segment* s2 ){
    Vec2 baseline = *(s2->r)-*(s2->l);
    Vec2 s1dir = *(s1->l)-*(s2->l);
    return s1dir.cross(baseline) > 0 ;
  }
  
private:
  int calculateDirection( const Vec2& p1, const Vec2& p2, const Vec2& p3 )const{
    //p1
    //p2 p3
    auto p12 = p1-p2;
    auto p13 = p1-p3;
    return p12.cross(p13);
  }
  
  bool withinRange( const Vec2& p1, const Vec2& p2, const Vec2& p3 )const{
    return ( p1.x >= min(p2.x, p3.x) && p1.x<=max(p2.x,p3.x) ) 
      &&   ( p1.y >= min(p2.y, p3.y) && p1.y<=max(p2.y,p3.y) );
  }

  bool intersection( const Vec2& p1, const Vec2& p2, const Vec2& p3, const Vec2& p4 ) const{
    //test if p12 p34 intersects
    int d134=calculateDirection( p1, p3, p4 );
    int d234=calculateDirection( p2, p3, p4 );
    int d312=calculateDirection( p3, p1, p2 );
    int d412=calculateDirection( p4, p1, p2 );
    bool b12 = (d134>0&&d234<0)||(d134<0&&d234>0);
    bool b34 = (d312>0&&d412<0)||(d312<0&&d412>0);
    if( b12 && b34 ){
      if( withinRange( p1,p3,p4 ) && withinRange( p2,p3,p4) ){
        return true;
      }
    }
    return false;
  }
  
};
struct EndPoint{
  EPType type;
  const Vec2* p;
  const Segment* s;
  EndPoint( const Vec2* pt, const Segment* sg, EPType tp ): p(pt),s(sg),type(tp){}
  
  static bool isLeftUp( const EndPoint* l, const EndPoint* r ){
    return !Vec2::isLeftUp( *(l->p), *(r->p) );
  }
};

bool scanLineTestSegmentsIntersection( const vector<Segment>& sg ){
  int n = sg.size();
  vector<EndPoint*> endPoints;
  for( int i=0; i<n; i++ ){
    Segment s = sg[i];
    //I was intended to use the stackobject here
    //but the compiler wont let me
    endPoints.push_back( &EndPoint( s.l, &s, EPType::Left ) );
    endPoints.push_back( &EndPoint( s.r, &s, EPType::Right ) );
  }
  sort( endPoints.begin(), endPoints.end(), EndPoint::isLeftUp );

  set<const Segment*, bool(*)(const Segment*, const Segment*) > segmentTree(Segment::Above);

  for( int i=0; i<2*n; i++ ){
    //EndPoint ep = *(endPoints[i]);
    EndPoint* ep = endPoints[i];
    if( ep->type == EPType::Left ){
      auto ret = segmentTree.insert( (ep->s) );
      if( ret.second == false ){
        printf("sth wrong\n");
      }
      auto itr = ret.first;
      auto pitr = prev(itr);
      if( pitr != segmentTree.end() ){
        Segment p = **pitr;
        Segment n = **itr;
        if( (p).Intersect(n) ) return true;
      }
      auto nitr = next(itr);
      if( nitr != segmentTree.end() ){
         Segment p = **itr;
         Segment n = **nitr;
         if( (p).Intersect(n) ) return true;

      }
    }
    else if ( ep->type == EPType::Right ){
      auto itr = segmentTree.find( ep->s );
      if( itr == segmentTree.end() ){
        printf("sth wrong finding \n");
      }
      auto pitr = prev(itr);
      auto nitr = next(itr);
      if( pitr != segmentTree.end() && nitr != segmentTree.end() ){
        Segment p = **pitr;
        Segment n = **nitr;
        if( p.Intersect(n) ) return true;
        segmentTree.erase(itr);
      }
    }
  }
  
  
  return false;
}

void TestSegmentCases( const Segment& s1, const Segment& s2, bool expected ){
  static int cases = 0 ;
  bool actual = s1.Intersect(s2);
  if(  actual == expected ){
    printf( "CASE:%d PASSED\n", cases );
  }
  else{
    printf( "CASE:%d FAILED, Expected:%d, But:%d\n", cases, expected, actual );
  }
  cases++;
}

void TestSegmentCollectionCases( const vector<Segment> segments , bool expected ){
  static int cases = 0 ;
  bool actual = scanLineTestSegmentsIntersection(segments );
  if(  actual == expected ){
    printf( "CASE:%d PASSED\n", cases );
  }
  else{
    printf( "CASE:%d FAILED, Expected:%d, But:%d\n", cases, expected, actual );
  }
  cases++;
}

void TestSegment(){
  Vec2 p00=Vec2(0,0),p01=Vec2(0,1),p10=Vec2(1,0),p11=Vec2(1,1);
  Segment s0001=Segment(p00,p01), s1011=Segment(p10,p11), s0011=Segment(p00,p11), s1001=Segment(p10,p01);
  TestSegmentCases(s0001,s1011, false);
  TestSegmentCases(s0011,s1001, true);
  
  vector<Segment> sample1;
  sample1.push_back( s0001 );
  sample1.push_back( s1011 );
  TestSegmentCollectionCases( sample1, false );

  vector<Segment> sample2;
  sample2.push_back( s0011 );
  sample2.push_back( s1001 );
  TestSegmentCollectionCases( sample2, true );

  vector<Segment> sample3;
  sample3.push_back( s0001 );
  sample3.push_back( s1011 );
  sample3.push_back( s0011 );
  sample3.push_back( s1001 );
  TestSegmentCollectionCases( sample3, true );
}


int main(){
  TestSegment();
  return 0;
}
