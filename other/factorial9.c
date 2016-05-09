#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

void mul(int* pa, int b, int m){
    for( int i=0;i<m;i++){
        pa[i]=pa[i]*b;
    }
    for( int i=0;i<m-1;i++){
        pa[i+1]+=pa[i]/10;
        pa[i]=pa[i]%10;
    }
}

int main() {
    int n=0;
    cin >> n;
    int n1=n;
    int n0=0;
    while(n1){
        n0+=(n1/5);
        n1/=5;
    }
    int m=n0+10;
    int* pa=new int[m];
    pa[0]=1;

    for( int i=1;i<n+1;i++){
        mul(pa,i,m);
    }
    int s=0;
    for( int i=m-2;i>=0;i--){
        if( pa[i]==0){
            continue;
        }
        s=i;
        break;
    }
    vector<int> r;
    for( int i=s;i>n0-1;i--){
        r.push_back(pa[i]);
    }

    for( int i=0;i<r.size();i++){
        cout << r[i];
    }
    cout << endl;

    delete []pa;

    return 0;
}


