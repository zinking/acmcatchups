#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>

#define DELIM '|'

using namespace std;

int FixMsgGetTagValue
( char *msg, int sizeOfMsg,                 // FIX message
  char *tagValue, int sizeOfTagValueBuffer, // Buffer to receive value
  char *tagStr, int sizeOfTagStrBuffer)     // Tag (e.g. 2-char string "52")
{
  int i=0, j=0;
  char temp_buffer[50] = "|";

  /* Initialize with blanks to prevent other initialization problems we were seeing */
  memcpy(&(temp_buffer[1]), tagStr, sizeOfTagStrBuffer);
  cout << temp_buffer << endl;
  sizeOfTagStrBuffer++;
  memcpy(&(temp_buffer[sizeOfTagStrBuffer]), "=", 1);
  sizeOfTagStrBuffer++;
  cout << temp_buffer << endl;
  cout << sizeOfTagStrBuffer << endl;
  for(i=0, j=0; i < sizeOfMsg; i++) {
    if(msg[i] == temp_buffer[j])
      j++;
    else {
      if(j)
	i--;
      j=0;
    }
    if(j == sizeOfTagStrBuffer)
      break;
  }
  cout << "i=" << i << endl;
  cout << "j=" << j << endl;
  
  if(j == sizeOfTagStrBuffer){
    for(j=0, i++; (msg[i]!=DELIM) && (j < sizeOfTagValueBuffer) &&
	  (i < sizeOfMsg); i++, j++)
      tagValue[j] = msg[i];
    tagValue[j] = '\0';
  } else
    j=0;
  return j;
}




int main(){
  vector<int> a;
  a.push_back( 10 );
  a.push_back( 20 );
  a[1] = 30;

  for( int i=0; i<a.size(); i++ )
    cout << a[i] << endl;
  printf("helloworld\n");


  char message[1000] = "8=FIX.4.2|152=abc|49=E|52=bc";
  char val[5];
  char tag[5]="52";
  FixMsgGetTagValue( message, strlen(message), val, 5, tag, 2 );

  cout << val << endl;
  return 0;
}
