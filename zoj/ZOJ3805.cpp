#include<cstdio>
#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>

using namespace std;

typedef vector<vector<int> > AdjArr;


int minGridWidth( const int nodeId, const AdjArr* pArr );
//3805 min width of grid for connected machines
//if node 2 takes min grid width of x and  node 3 takes MGW of y
//then final node takes max(x,y)-1 as we can make them share along the height

int minGridWidth( const int nodeCount, const int* pArr ){
  AdjArr adjArr(nodeCount);
  for( int i=0; i<nodeCount; i++ ){
    int adji = pArr[i];
    if( adji != -1 ){
      //adjArr[adji].push_back( i ); //0 index based
      adjArr[adji-1].push_back( i );
    }
  }
  return minGridWidth(0, &adjArr);
}

int minGridWidth( const int nodeId, const AdjArr* pArr ){
  vector<int> adjNodes = (*pArr)[nodeId];
  int sz = adjNodes.size();
  if( sz == 0 ){
    return 1;
  }
  else if ( sz == 1 ){
    int n1 = adjNodes[0];
    return minGridWidth( n1, pArr);
  }
  else if ( sz == 2 ){
    int n1 = adjNodes[0];
    int n2 = adjNodes[1];
    int n1c = minGridWidth( n1, pArr );
    int n2c = minGridWidth( n2, pArr );
    //return max( n1c, n2c ) -1;
    if( n1c < n2c ){
      int temp = n1c;
      n1c = n2c;
      n2c = temp;
    }
    return max( n1c-1, n2c ) + 1;
  }

  printf("something terribly wrong happened\n");
  return 0;
}

int runTestCases( const int nodeCount, const int* pArr, int expected ){
  static int count = 0;
  int actual = minGridWidth( nodeCount, pArr);
  if( actual == expected ){
    printf("Case NO:%d, PASSED\n", count );
  }
  else{
    printf("Case NO:%d, FAILED, expected[%d] Actual[%d]\n", count, expected,actual);
  }
  count++;
  return 0;
}

int main0(){
  int adjArr1[2] = {-1,1};
  runTestCases( 2, adjArr1, 1);
  int adjArr2[3] = {-1,1,1};
  runTestCases( 3, adjArr2, 2);
  int adjArr3[7] = {-1,1,1,2,2,3,3};
  runTestCases( 7, adjArr3, 3);
  return 0; 
}

int main(){
  int raw[10001];
  raw[0]=-1;
  while( !cin.eof() ){
    int cnt = 0;
    cin >> cnt;
    for( int i=1; i<cnt; i++ ){
      cin >> raw[i];
      raw[i]--;
    }
    int result = minGridWidth(cnt,raw);
    printf("%d\n",result);
  }
}
