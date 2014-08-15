#include<cstdio>
#include<cstdlib>
#include<vector>
#include<cmath>

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

};

struct Segment{
  const Vec2* l;
  const Vec2* r;
  Segment(const Vec2&ll, const Vec2& rr):l(&ll),r(&rr){}
  
  bool Intersect( const Segment& rhs )const{
    return intersection( *l,*r, *(rhs.l), *(rhs.r) );
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
  EndPoint( const Vec2* pt, const Segment* sg, EPType tp ):
    p(pt),s(sg),type(tp){}
  
};

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
void TestSegment(){
  Vec2 p00=Vec2(0,0),p01=Vec2(0,1),p10=Vec2(1,0),p11=Vec2(1,1);
  Segment s0001=Segment(p00,p01), s1011=Segment(p10,p11), s0011=Segment(p00,p11), s1001=Segment(p10,p01);
  TestSegmentCases(s0001,s1011, false);
  TestSegmentCases(s0011,s1001, true);
  
}


int main(){
  TestSegment();
  return 0;
}
