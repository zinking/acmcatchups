#include <iostream>
#include <vector>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <sstream>
using namespace std;


class Solution {
public:
  int evalRPN(vector<string> &tokens) {
    stack<string,vector<string> > tks(tokens);
    stack<int> nums;
    stringstream ss;
    while( !tks.empty() ){
      string r = tks.top();
      if( isOperator(r) ){
	int op1 = nums.top();
	nums.pop();
	int op2 = nums.top();
	nums.pop();
	switch( r.at(0)){
	case '+':
	  nums.push( op1+op2 );
	  break;
	case '-':
	  nums.push( op1-op2 );
	  break;
	case '*':
	  nums.push( op1*op2 );
	  break;
	case '/':
	  nums.push( op1/op2 );
	  break;
	default:
	  throw( "unexpected operator");
	}
      }
      else{//assumption is made that input is either operator or number
	ss << r ;
	int num;
	ss >> num;
	ss.flush();
	nums.push(num);
      }
        	
    }
    return nums.top();
  }
    
  bool isOperator( string& r ){
    if( r.length() ==1 ){
      char c = r.at(0);
      if( c == '+' || c=='-' || c=='*' || c=='/'){
	return true;
      }
    }
    return false;
  }
};


void test_solution( int no, vector<string>& input, int expected ){
  Solution s;
  int actual = s.evalRPN( input );
  if( actual == expected ){
    printf( "Case %d: Passed." , no );
  }
  else{
    printf( "Case %d: Failed. Actual [%d], Expected [%d]." , no, actual, expected );
  }
}

int main() {
  // your code goes here
  vector<string> c1 = {"2", "1", "+", "3", "*"};
  test_solution( 1, c1, 9);
  vector<string> c2 = {"4", "13", "5", "/", "+"};
  test_solution( 2, c2 , 6);
  return 0;
}
