#include <stdio.h>
#include <math.h>
#include <string.h>

int calR(int n) {
	int r = 1;
	while (1) {
		if (pow(2, r-1) <= n+r && pow(2, r) > n+r) {
			break;
		}
		++r;
	} 
	return r;
}

void sendMessage(int n, char *msg) {
	int r = calR(n);
	// Todo: :)
}

int main() {
	char str[127];
	scanf("%s", str);
	int n = strlen(str);
	printf("%d\n", calR(n));
	return 0;
}
