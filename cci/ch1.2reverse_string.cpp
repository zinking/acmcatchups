#include<iostream>

using namespace std;

void r_str( char* str ){
  char* h=str;
  char* t=str;
  while( *(t+1) ) t++;
  for( ; h<t; h++,t-- ){
    char tmp = *h;
    *h = *t;
    *t = tmp;
  }
}


int main(){
  char str1[10]="abcdefg";
  r_str(str1);
  cout << "reverse string [abcdefg]:" << str1 << endl;
  char str2[10]="AbcDefg";
  r_str(str2);
  cout << "reverse string [AbcDefg]:" << str2 << endl;
  char str3[10]="1bcd2fg";
  r_str(str3);
  cout << "reverse string [1bcd2fg]:" << str3 << endl;
  
  return 0;
}

