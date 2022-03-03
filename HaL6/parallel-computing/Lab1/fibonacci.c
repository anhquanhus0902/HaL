#include <stdio.h>

int fibonacci(int n) {
	if (n < 2) {
		return n;
	}
	return fibonacci(n-2) + fibonacci(n-1);
}

int main() {
	int n;
	scanf("%d", &n);
	printf("%d", fibonacci(n));
	return 0;
}