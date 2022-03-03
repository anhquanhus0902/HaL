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

void solve(long n, int m) {
	if (m == 0) {
		return;
	}
	while (m) {
		if (isPrime(n)) {
			--m;
			if (!m) {
				break;
			}
		}
		if (n % 2 == 0) {
			++n;
		}
		else {
			n += 2;
		}
	}
	printf("%ld", n);
}

int main() {
	long n;
	int m;
	scanf("%ld %d", &n, &m);
	solve(n, m);
	return 0;
}