#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverseWords(char *s) {
    int n = strlen(s);
    int ps = 0, pe = 0;
    while (ps<n) {
        while (ps<n && s[ps] != ' ') ps++;
        pe = ps;
        while (pe<n && s[pe] == ' ') pe++;
        if ((pe>ps+1 || ps==0) && pe<n) {
            int i1=pe;
            int j1= ps==0?0:ps+1;
            while (i1<=n) {
                s[j1] = s[i1];
                i1++;
                j1++;
            }
          
        }

        if (pe == n) {
            s[ps] = s[n];
        }
        ps++;
        n = strlen(s);
    }

    int i = 0, j = n-1;
    while (i<j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
	i++;
 	j--;
    }
    
    int p = 0;
    i = 0;
    while (p<n){
        while (p<n && s[p] != ' ') p++;
        j = p-1;
        while (i<j) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
	    i++;
            j--;
        }
        i = p+1;
        p+=1;
    }
}

int main() {
    char str1[] = "    hello  world        ds   "; 
    reverseWords(str1);
    printf("%s$\n",str1);

    char str2[] = " 1";
 
    reverseWords(str2);
    printf("%s$\n",str2);
    return 0;
}
