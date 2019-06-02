#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
const int N = 100;
int H, B, v, hot[N], bun[N], sumH = 0, sumB = 0;
int main()
{
    //ifstream cin("in");
    cin >> H;
    for (int i = 0; i < H; i++)
    {
        cin >> hot[i];
        sumH += hot[i];
    }
    cin >> B;
    for (int i = 0; i < B; i++)
    {
        cin >> bun[i];
        sumB += bun[i];
    }
    int C = min(sumB, sumH) + 1, D = max(H, B);
    int inf = 1 << 29;
    vi SH(C, inf), SB(C, inf);
    SH[0] = SB[0] = 0;
    for (int k = 0; k < H; k++)
    {
        int i = hot[k];
        for (int s = C - i - 1; s >= 0; s--)
            if (SH[s] < SH[s + i])
                SH[s + i] = SH[s] + 1;
    }
    for (int k = 0; k < B; k++)
    {
        int i = bun[k];
        for (int s = C - i - 1; s >= 0; s--)
            if (SB[s] < SB[s + i])
                SB[s + i] = SB[s] + 1;
    }
    /*for (int i = 0; i < 25; i++)
        printf("%d->%d\n", i, SB[i]);*/
    int min_v = inf;
    for (int i = 1; i < C; i++)
        if (SH[i] != inf && SB[i] != inf)
            min_v = min(SH[i] + SB[i], min_v);
    if (min_v !=inf )
        cout << min_v << endl;
    else
        cout << "impossible";
}