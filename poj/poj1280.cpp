#include <iostream>
using namespace std;

#define L 3

float P[2L-1][L][2];

void calculateP( float Pa, float Pb ){
  int i=0,j=0;
  for( i=1;i<2*L-1;i++ ){
    for( j=1
