#include <bits/stdc++.h>
using namespace std;
const int N = 100000;
void print(int t[], int n)
{
    for (int i = 0; i < n; i++)
        cout << t[i] << " ";
    cout << endl;
}
int main()
{
    //int A[] = {-7, 10, 9, 2, 3, 8, 8, 1, 2, 3, 4};
    //ifstream cin("in");
    int A[N], n;
    while (cin >> n)
    {
        int L[N], lis = 0, lis_end = 0, L_id[N], P[N];
        for (int i = 0; i < n; i++)
        {
            cin >> A[i];
            int pos = lower_bound(L, L + lis, A[i]) - L;
            L[pos] = A[i];
            L_id[pos] = i;
            P[i] = pos ? L_id[pos - 1] : -1;
            if (pos + 1 > lis)
            {
                lis = pos + 1;
                lis_end = i;
            }
        }
        stack<int> s;
        cout << lis << endl;
        s.push(lis_end);
        for (int x = lis_end; P[x] >= 0; x = P[x])
            s.push(P[x]);
        printf("%d", s.top());
        s.pop();
        for (; !s.empty(); s.pop())
            printf(" %d", s.top());
        cout << endl;
        //print(L, n);
        //print(P, n);
    }
}