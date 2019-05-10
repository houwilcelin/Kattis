/* 
 * File:   nonprime.cpp
 * Author: Jocelin
 *
 * Created on 13 mars 2019, 10:20
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <math.h>
#define P(p)  point &p
#define pi(p)  perm[p]
#define L(p0, p1) P(p0), P(p1)
#define r(v) ((v+1)%7)
using namespace std;
struct point {
    double x,y;
    point(){
        x=0;y=0;
    }
    point(double _x, double _y) {
        x = _x, y = _y;
    }
    point operator+(const point &oth){
        return point(x + oth.x, y + oth.y);
    }
    point operator-(const point &oth){
        return point(x - oth.x, y - oth.y);
    }
};
double cross(P(a),P(b)){
    return a.x*b.y - a.y*b.x;
}
double ccw(P(a), P(b), P(c)) {
    //(bx 􀀀 ax )(cy 􀀀 ay ) 􀀀 (by 􀀀 ay )(cx 􀀀 ax ) > 0.
    point ab = b-a,ac = c-a;
    return (b.x-a.x)*(c.y-a.y) - (b.y - a.y)*(c.x-a.x);
}
bool left(P(a), P(b), P(c)){
    return ccw(a, b, c) > 0;
}
double is_cross(P(a), P(b),P(c),P(d)) {
    return left(a, b, c) != left(a, b, d) && left(c, d, a) != left(c, d, b);
}
bool is_simple(point *points,int perm[]){
    int n = 7;
    for(int i = 0;i <n;i++){
        for (int j = i+2;j<n;j++){
            if (((j+1) % n) != i){
                bool is_c = is_cross(points[pi(i)], points[pi(i +1)], points[pi(j)], points[pi((j+1) % n)]);
                if (is_c) return false;
            }
        }
    }
    return true;
}
double polygon_area(point *p, int perm[]) {
    double area = 0;
    for (int i = 0; i < 7; i++){
        /*point aa=p[pi(i)] - p[pi(0)];
        point ab= p[pi(i + 1)] - p[pi(0)];
        area += cross(aa,ab)/2;*/
        area += p[perm[r(i)]].x * (p[perm[r(i+1)]].y - p[perm[r(i-1)]].y);
    }
    return abs(area / 2.0);
}
void out(int p[],int t){
    printf("%d %d %d %d %d %d %d\n",p[0]+1,p[1]+1,p[2]+1,p[3]+1,p[4]+1,p[5]+1,p[6]+1);
}
int main(int argc, char** argv) {
    int c;
    scanf("%d",&c);
    point points[7];
    while(c--){
        for (int i=0;i < 7; i++){
            double x,y;
            scanf("%lf %lf",&x,&y);
            points[i] = point(x,y);
            //printf("Create point (%lf:%lf)\n",x,y);
        }
        double proba;
        scanf("%lf",&proba);
        double proba_l = proba - 1E-5;
        double proba_r = proba + 1E-5;
        //printf("Read proba (%lf)\n",proba);
    
        //int perm[7] = {1,2,3,4,5,6,7};
        int perm[7] = {0,1,2,3,4,5,6};
        do{
            double a_ = pow(polygon_area(points, perm) / 4.0,3);
            if (a_ < proba_r && proba_l < a_ && is_simple(points,perm)){
                out(perm,7);
                break;
                //cout << ":" << a__ <<endl;
            }
            //out(perm,7);
        }while(next_permutation(perm,perm+7));
        /*int v[7] = {0,1,2,6,4,5,3};//1,2,3,7,5,6,4};
        cout << "\nYs:"<<pow(polygon_area(points, v) / 4.0,3);*/
    }
}