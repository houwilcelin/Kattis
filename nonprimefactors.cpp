/*
 * File:   nonprime.cpp
 * Author: Jocelin
 *
 * Created on 13 mars 2019, 10:20
 */

#include <cstdlib>
#include <cstdio>
using namespace std;
const int MAX = 2000001;
int divi[MAX];
int f[MAX];
int p[MAX];
int count(int i,int j) {
    int r = 0;
    while(j%i == 0) {
        r++;
        j/=i;
    }
    return r;
}
/*
 *
 */
int main(int argc, char** argv) {
    for (int i=0; i<MAX; i++) {
        f[i] = 1;
        p[i] = 0;
    }
    for (int i = 2; i < MAX; i++) {
        if (p[i] == 0) { // if i is prime
            for (int j = i*2; j<MAX; j+=i) {
                f[j]*=1+count(i,j);
                p[j] += 1;
            }
        }
    }
    //printf("%d",f[100]);
    int c,n;
    scanf("%d",&c);
    while(c--) {
        scanf("%d",&n);
        printf("%d\n",f[n]-p[n]);
    }
    return 0;
}
