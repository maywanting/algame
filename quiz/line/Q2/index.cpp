#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define lp (p << 1)
#define rp (p << 1|1)
#define getmid(l,r) (l + (r - l) / 2)
#define MP(a,b) make_pair(a,b)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
const int INF = (1 << 30) - 1;
const int maxn = 110;

int num[10], L[21], R[21], tot = 9;
string ans[10];

struct cmp{
    bool operator ()(pii a,pii b){
        return a.first > b.first;
    }
};

void Dfs(int p, string cur){
    if(L[p] == p){
        //cout << p << " : " << cur << endl;
        ans[p] = cur;
        return;
    }
    Dfs(L[p], cur + "0");
    Dfs(R[p], cur + "1");
    return;
}

int main(int argc, char *argv[]) {
    // start from 1 to ignore script name; argv[0] will be a name of processing file.
    for (int i = 1; i < argc; i++) {
        //cout << "argv[" << i << "]:" << argv[i] << "\n";
        int len = strlen(argv[i]);
        for(int j = 0; j < 21; ++j){
            L[j] = R[j] = j;
        }
        priority_queue<pii,vector<pii >,cmp> PQ;
        for(int j = 0; j < 10; ++j){
            num[j] = 0;
        }
        for(int j = 0; j < len; ++j){
            num[argv[i][j] - '0']++;
        }
        int count = 0;
        for(int j = 0; j < 10; ++j) if(num[j] > 0){
            PQ.push(make_pair(num[j], j));
            //cout << j << " : " << num[j] << endl;
            count += 1;
        }
        if(count == 1){
            for(int j = 0; j < 10; ++j){
                cout << j << " " << (num[j] ? "0" : "null") << endl;
            }
            continue;
        }
        while(!PQ.empty()){
            pii now = PQ.top();
            PQ.pop();
            if(PQ.empty()){
                break;
            }
            pii now2 = PQ.top();
            PQ.pop();
            pii next = pii(now.first + now2.first, ++tot);
            L[tot] = now.second;
            R[tot] = now2.second;
            PQ.push(next);
            //cout << now.first << now.second << endl;
        }
        Dfs(tot, string(""));
        for(int j = 0; j < 10; ++j){
            cout << j << " " << (num[j] ? ans[j] : "null") << endl;
        }
    }
    return 0;
}
