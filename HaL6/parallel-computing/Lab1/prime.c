#include <stdio.h>
#include <math.h>

int isPrime(long n) {
	if (n < 2) {
		return 0;
	}
	for (int i = 2; i <= sqrt(n); ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}

long solve(int l) {
	if (l < 1) {
		return -1;
	}
	long minNumber = 1;
	for (int i = 1; i < l; ++i) {
		minNumber *= 10;
	}
	++minNumber;
	while (!isPrime(minNumber)) {
		minNumber += 2;
	}
	return minNumber;
}

int main() {
	int l;
	scanf("%d", &l);
	printf("%ld", solve(l));
	return 0;
}