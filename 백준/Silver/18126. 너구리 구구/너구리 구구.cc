#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#define MAX 5001
#define INF 5e12+1
#define LL long long
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;
int N, A, B;
LL C;
vector<pair<int, LL> > Edge[MAX];
LL Dist[MAX];
LL Answer;

void init() {
    for (int i = 0; i < MAX; i++) {
        Dist[i] = INF;
    }
}

void input() {
    cin >> N;
    for (int i = 0; i < (N - 1); i++) {
        cin >> A >> B >> C;
        Edge[A].push_back(make_pair(B, C));
        Edge[B].push_back(make_pair(A, C));
    }
}

void BFS() {
    Dist[1] = 0;
    queue<pair<int, LL> > Q;
    Q.push(make_pair(1, 0));

    while (!Q.empty()) {
        int NowX = Q.front().first;
        LL NowC = Q.front().second;
        Q.pop();

        for (int i = 0; i < Edge[NowX].size(); i++) {
            int NextX = Edge[NowX][i].first;
            LL NextC = Edge[NowX][i].second;
            if (Dist[NextX] > NowC + NextC) {
                Dist[NextX] = NowC + NextC;
                Q.push(make_pair(NextX, Dist[NextX]));
            }
        }
    };
}

void settings() {
    BFS();
    for (int i = 1; i <= N; i++) {
        Answer = max(Answer, Dist[i]);
    }
}

void find_Answer() {
    cout << Answer << "\n";
}

int main() {
    FASTIO
    init();
    input();
    settings();
    find_Answer();

    return 0;
}