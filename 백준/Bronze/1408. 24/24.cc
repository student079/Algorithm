// 정렬 : ctrl + k + f
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
using namespace std;

struct Time {
	int hour, minute, second;
};

int time2int(Time time);

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	Time current, start;

	scanf("%d:%d:%d", &current.hour, &current.minute, &current.second);
	scanf("%d:%d:%d", &start.hour, &start.minute, &start.second);

	int currentInt = time2int(current);
	int startInt = time2int(start);

	if (currentInt < startInt) {
		int resultInt = startInt - currentInt;
		printf("%02d:%02d:%02d", resultInt / 3600, resultInt % 3600 / 60, resultInt % 60);
	}
	else {
		int resultInt = 24 * 3600 - currentInt + startInt;
		printf("%02d:%02d:%02d", resultInt / 3600, resultInt % 3600 / 60, resultInt % 60);
	}

	return 0;
}

int time2int(Time time) {
	return time.hour * 60 * 60 + time.minute * 60 + time.second;
}