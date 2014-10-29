
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
  
inline  double findMedianSortedArray(int A[], int m){
    return m&1 ? A[m/2] : double(A[m/2]+A[m/2-1])/2.0;
  }

  double findMedianSortedArrayBase2( int pA*, int m, int pB*, int n ){
    // this is making time complexity o(nlogn) worst case
    // when [ x y ] [ ... x1 x2 x3 x4 x5 ..] is combined 
    // case 1:x x3 y , then median still x3
    // case 2:x y x3 , then median become x2 

    if( m > n ){
      int tmp;
      int* ptmp;
      tmp = n, n=m, m=tmp;
      ptmp = pB, pB=pA, pA= ptmp; 
    }
    // pA is the 2 element array
    
    


  }
  
  double findMedianSortedArrayBase(int A[], int m, int B[], int n ){
    vector<int> AB(A,A+m);
    AB.insert(AB.end(), B, B+n);
    sort( AB.begin(), AB.end() );
    int sz = m+n;
    return sz & 1 ? AB[sz/2]: double( AB[sz/2]+AB[sz/2-1] )/2.0;
  }
  double findMedianSortedArrays(int A[], int m, int B[], int n) {
    if( m==0 ){
      return findMedianSortedArray(B,n);
    }
    else if( n==0 ){
      return findMedianSortedArray(A,m); 
    }
    else if( m <=2 || n<=2 ){
      return findMedianSortedArrayBase(A,m,B,n);
    }
    else{
      double ma = findMedianSortedArray(A,m);
      double mb = findMedianSortedArray(B,n);

      //elements that could be removed from 2 sides
      int sa = m&1 ? (m-1)/2 : (m-2)/2;
      int sb = n&1 ? (n-1)/2 : (n-2)/2;
      int nn = fmin( sa,sb );
      //printf( "ma %g mb %g m %d n %d nn %d \n", ma,mb,m,n,nn);
      if( ma > mb ){
        return findMedianSortedArrays( B+nn,n-nn, A, m-nn);
      }
      else if( ma == mb ){
        //simple proof, two sides of median have same amount of number
        //so if combined, still they are medians
        return ma;
      }
      else{
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
  int A9[4] = {4,5,6,8};
  int B9[6] = {1,2,3,7,9,10};
  actual = s1.findMedianSortedArrays(A9,4,B9,6);
  testcase(5.5,actual);

  int A10[4] = {1,5,6,7};
  int B10[6] = {2,3,4,8,9,10};
  actual = s1.findMedianSortedArrays(A10,4,B10,6);
  testcase(5.5,actual);


  int A8[4] = {1,2,6,7};
  int B8[4] = {3,4,5,8};
  actual = s1.findMedianSortedArrays(A8,4,B8,4);
  testcase(4.5,actual);

  int A7[3] = {1,2,6};
  int B7[3] = {3,4,5};
  actual = s1.findMedianSortedArrays(A7,3,B7,3);
  testcase(3.5,actual);

  int A6[1] = {2};
  int B6[3] = {1,3,4};
  actual = s1.findMedianSortedArrays(A6,1,B6,3);
  testcase(2.5,actual);

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
