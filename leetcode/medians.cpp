
#include <cstdio>
#include <cmath>

using namespace std;

// {} {1,2,3}

class Solution {
public:
  double findMedianSortedArray(int A[], int m ){
    if( m&1 ){ //odd
      int mid = m/2;
      return A[mid];
    }
    else{
      int mid1 = m/2;
      int mid2 = m/2-1;
      return (A[mid1]+A[mid2])/2.0f;
    }
  }
  double findMedianSortedArrays(int A[], int m, int B[], int n) {
    if( m==0 ){
      return findMedianSortedArray(B,n);
    }
    else if( n==0 ){
      return findMedianSortedArray(A,m); 
    }
    else if( m==1 && n==1 ){
      return double(A[0]+B[0])/double(2.0);
    }
    else{
      int ma = A[m/2];
      int mb = B[n/2];
      int nn = fmin( round((float)n/2), round((float)m/2) );
      if( ma > mb ){
        return findMedianSortedArrays( B+nn,n-nn, A, m-nn);
      }
      else{
        //1   -> mid 0 midvalue 1
        //2 3 -> mid 1 midvalue 3
        // it must be combined to be 1 .... 3 and median between them
        // so drop 1, 3 
        return findMedianSortedArrays( A+nn,m-nn, B, n-nn );
      }
    }
  }
};
//{1,2} {3,4,5}

void testcase( double expected, double actual ){
  static int caseno = 0;
  if( expected == actual ){
    printf( "case %d SU\n", caseno );
  }
  else{
    printf( "case %d FA -- Actual:%f Expected %f \n", caseno, actual, expected );
  }
  caseno++;
}


int main(){
  Solution s1;
  double actual = -1;
  int A[4] = {5,6,7,8};
  int B[4] = {1,2,3,4};
  actual = s1.findMedianSortedArrays(A,4,B,4);
  testcase( 4.5, actual );

  int AA[1] = {1};
  int BB[1] = {2};
  actual = s1.findMedianSortedArrays(AA,1,BB,1);
  testcase( 1.5, actual );

  int AAA[0] = {};
  int BBB[1] = {1};
  actual = s1.findMedianSortedArrays(AAA,0,BBB,1);
  testcase( 1, actual );
  
  int A1[0] = {};
  int B1[3] = {1,2,3};
  actual = s1.findMedianSortedArrays(A1,0,B1,3);
  testcase( 2, actual );
  
  int A2[0] = {};
  int B2[5] = {1,2,3,4,5};
  actual = s1.findMedianSortedArrays(A2,0,B2,5);
  testcase( 3, actual );

  
  int A3[2] = {1,2};
  int B3[3] = {3,4,5};

  actual = s1.findMedianSortedArrays(A3,2,B3,3);
  testcase( 3, actual );
  

  int A4[3] = {1,2,3};
  int B4[3] = {4,5,6};

  actual = s1.findMedianSortedArrays(A4,3,B4,3);
  testcase( 3.5, actual );

  int A5[3] = {1,2,3};
  int B5[3] = {1,2,2};

  actual = s1.findMedianSortedArrays(A5,3,B5,3);
  testcase(2,actual);

  return 0;
}
