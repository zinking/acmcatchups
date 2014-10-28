
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

    if( m==1 && n==0 ){
      return A[0];
    }
    else if( m==0 && n==1 ){
      return B[0];
    }
    else if( m==1 && n==1 ){
      return double(A[0]+B[0])/2;
    }
    else if ( m==1 && n==2 ){
      return B[0];
    }
    else if ( m==2 && n==1 ){
      return A[1];
    }
    else if( m==0 ){
      return findMedianSortedArrays( B, n/2, &B[n/2], n-n/2);
    }
    else if( n==0 ){
      return findMedianSortedArrays( A, m/2, &A[m/2], m-m/2);
    }
    else{
      int ma = A[m/2];
      int mb = B[n/2];
      int ham = round( m/2.0f );
      int hbn = round( n/2.0f );
      if( ma >= mb ){
        //5 6 7 8 => 7
        //1 2 3 4 => 3
        return findMedianSortedArrays( &B[n/2], n-hbn, A, ham );
      }
      else{
        return findMedianSortedArrays( &A[m/2], m-ham, B, hbn);
      }
    }
  }
};


int main(){
  Solution s1;
  int A[4] = {5,6,7,8};
  int B[4] = {1,2,3,4};
  printf("%g\n", s1.findMedianSortedArrays(A,4,B,4));

  int AA[1] = {1};
  int BB[1] = {2};
  printf("%g\n", s1.findMedianSortedArrays(AA,1,BB,1));

  int AAA[0] = {};
  int BBB[1] = {1};
  printf("%g\n", s1.findMedianSortedArrays(AAA,0,BBB,1));
  
  int A1[0] = {};
  int B1[3] = {1,2,3};
  printf("%g\n", s1.findMedianSortedArrays(A1,0,B1,3));
  
  int A2[0] = {};
  int B2[5] = {1,2,3,4,5};
  printf("%g\n", s1.findMedianSortedArrays(A2,0,B2,5));

  int A3[2] = {1,2};
  int B3[3] = {3,4,5};

  printf("%g\n", s1.findMedianSortedArrays(A3,2,B3,3));
  

  int A4[3] = {1,2,3};
  int B4[3] = {4,5,6};

  printf("%g\n", s1.findMedianSortedArrays(A4,3,B4,3));

  return 0;
}
