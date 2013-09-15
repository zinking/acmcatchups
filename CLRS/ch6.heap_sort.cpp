#include <iostream>
#include <algorithm>
#include <gtest/gtest.h>

using namespace std;

const int N=10;
int swap( int& a, int& b ){
  int temp = a;
  a = b;
  b = temp;
}

void max_heapify( int* a, int i, int sz ){
  int l = i*2, m=i;
  if( l <= sz && a[l] < a[i] ) m = l;
  int r = l+1;
  if( r <= sz && a[r] < a[m] ) m = r;
  if( m != i ) {
    swap( a[m], a[i] );
    max_heapify( a, m, sz );
  }
}

void heap_adj( int* a, int sz ){
  //for( int i=0; i<sz/2; i++ ){//from bottom to top
  for( int i=sz/2; i>=1; i-- ){
    max_heapify( a, i, sz );
  }
}

void heap_sort( int* a, int p, int q ){
  int sz = q-p+1;
  while( sz > 1 ){
    //heap_adj( &a[q-sz+1],sz);
    heap_adj( &a[q-sz],sz);
    sz--;
  }
}




TEST(SORTTEST, HandleNoneZeroInput)
{
  int a[11]={-1,10,9,8,7,6,5,4,3,2,1};
  heap_sort( a, 1, 10 );
  copy( a, a+10, ostream_iterator<int>(cout));
  cout << endl;
  EXPECT_EQ( a[1], 1 );
  EXPECT_EQ( a[2], 2 );
  EXPECT_EQ( a[10], 10);
}

int main( int argc, char* argv[] ){
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}


