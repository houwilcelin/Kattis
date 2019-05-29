#include <bits/stdc++.h>
#define N 8
using namespace std;
typedef pair<int, int> pii;
char c;
vector<int> row(N);
bool can_place(int r, int c)
{
    for (int prev = 0; prev < c; prev++)
        if (row[prev] == r || (abs(row[prev] - r) == abs(prev - c)))
            return false;
    return true;
}
bool isvalid()
{
    for (int c = 1; c < N; c++)
        if (!can_place(row[c], c))
            return false;
    return true;
}
int main()
{
    row.assign(N, 0);
    int nbr = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            cin >> c;
            if (c == '*')
            {
                row[j] = i;
                nbr++;
            }
        }

    if (row.size() == 8 && isvalid())
        cout << "valid";
    else
        cout << "invalid";
    return 0;
}