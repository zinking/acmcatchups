#include<iostream>
#include<stack>


using namespace std;

stack<int> stack_sort( stack<int> s ){
  stack<int> r;
  while( !s.empty() ){
    int c = s.top();
    s.pop();
    while( !r.empty() && r.top() < c ){
      s.push( r.top() );
      r.pop();
    }
    r.push(c);
  }
  return r;
}


int main(){
  stack<int> s;
  s.push(4);
  s.push(1);
  s.push(2);
  s.push(3);
  stack<int> ss = stack_sort( s );
  
  while( !ss.empty() ){
    cout << ss.top() << " ";
    ss.pop();
  }
  return 0;
}

