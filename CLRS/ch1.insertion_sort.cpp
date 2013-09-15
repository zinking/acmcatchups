#include <iostream>
#include <algorithm>
#include <gtest/gtest.h>

using namespace std;

const int N=10;

void insert_sort( int* a, const int sz ){
  int i=0,j=0;
  for( j=1; j<sz; j++ ){
    i = j-1;
    int kk = a[j];
    while( i>=0 && a[i]>kk ){
      a[i+1]=a[i];
      --i;
    }
    a[i+1] = kk;//made 1 mistake here, 
  }
}

TEST(SORTTEST, HandleNoneZeroInput)
{
  int a[10]={10,9,8,7,6,5,4,3,2,1};
  insert_sort( a, 10 );
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


/*
void insert_sort( int* a, const int sz ){
    int i=0,j=0;
    for( j=1; j<sz; j++ ){
        int kk=a[j];
	i=j-1;
	while( i>=0 && a[i] > a[j] ){
	    a[i+1]=a[i];
	    --i;
	}
	a[i+1] = kk;
    }
}
 */
