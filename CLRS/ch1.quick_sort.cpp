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

int partition( int* a, int p, int q){
  int x=a[p];
  int j = p+1, i=j-1;
  while( j<=q ){
    if( a[j] < x ){
      swap( a[i+1], a[j] );
      i++;
    }
    j++;
  }
  swap( a[p], a[i] );
  return i;
}

void quick_sort( int* a, int p, int q ){
  if( p<q ){
    int m = partition( a, p, q );
    quick_sort( a, p, m );
    quick_sort( a, m+1, q );
  }
}




TEST(SORTTEST, HandleNoneZeroInput)
{
  int a[10]={10,9,8,7,6,5,4,3,2,1};
  quick_sort( a, 0, 9 );
  copy( a, a+10, ostream_iterator<int>(cout));
  cout << endl;
  EXPECT_EQ( a[0], 1 );
  EXPECT_EQ( a[1], 2 );
  EXPECT_EQ( a[9], 10);
}

int main( int argc, char* argv[] ){
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}


