
// 입구에서 가장 먼 방 구하기
// N 5000
// BFS 5000*log(5000)
// C 10억 long long

using namespace std;
#include <iostream>
#include <vector>
#include <queue>
#define FASTIO cin.tie(0); ios::sync_with_stdio(0);
#define MAX 5001
int N, A, B;
long long C;
long long answer;
vector<pair<int, long long>> graph[MAX];
long long dist[MAX];


void input() {
	cin >> N;
	for (int i = 0; i < N - 1; i++) {
		cin >> A >> B >> C;
		graph[A].push_back(make_pair(B, C));
		graph[B].push_back(make_pair(A, C));
	}
}

void init() {
	for (int i = 0; i < MAX; i++) {
		dist[i] = 5e12 + 1;
	}
}

void BFS() {
	dist[1] = 0;
	queue<pair<int, long long>> q;
	q.push(make_pair(1, 0));

	while (!q.empty()) {
		int node = q.front().first;
		long long d = q.front().second;
		q.pop();

		for (int i = 0; i < graph[node].size(); i++) {
			int nextNode = graph[node][i].first;
			long long nextD = graph[node][i].second;
			if (dist[nextNode] > d + nextD) {
				dist[nextNode] = d + nextD;
				q.push(make_pair(nextNode, dist[nextNode]));
			}
		}
	}
}

void getAnswer() {
	for (int i = 1; i <= N; i++) {
		answer = max(answer, dist[i]);
	}
	cout << answer << "\n" ;
}

int main(void) {
	FASTIO
	input();
	init();
	BFS();
	getAnswer();

	return 0;
}