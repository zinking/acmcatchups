#include <iostream>
#include <algorithm>
#include <gtest/gtest.h>

using namespace std;

const int N=10;

template<class T>
void merge( T* a, const int p, const int m, const int q );


template<class T>
void merge_sort( T* a, const int p, const int q){ //p first index q last index
  if( p<q ){
    int m = (p+q)/2;
    merge_sort<T>(a, p, m );
    merge_sort<T>(a, m+1, q );
    merge<T>( a, p, m , q );
  }
}

template<class T>
void merge( T* a, const int p, const int m, const int q ){
  T* b = new T[q-p+1+2];//add two guards
  int l=p-p,r=m+1-p+1;
  memcpy( b, &a[p], (m-p+1)*sizeof(T) );
  b[m+1] = 0x0FFFFF;
  memcpy( &b[r], &a[m+1], ( q-m-1+1 )*sizeof(T));
  b[q-p+1+1] = 0x0FFFFF;
  for( int i=p; i<=q; i++ ){
    if( b[l] <= b[r] ){
      a[i] = b[l];
      l++;
    }
    else{
      a[i] = b[r];
      r++;
    }
  }

  delete []b;
}


TEST(SORTTEST, HandleNoneZeroInput)
{
  int a[10]={10,9,8,7,6,5,4,3,2,1};
  merge_sort<int>( a, 0, 9 );
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


