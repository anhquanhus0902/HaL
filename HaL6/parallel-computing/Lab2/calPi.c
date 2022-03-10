#include <stdio.h>
#include <math.h>

double calPi(int n) {
	int i = 1, m = 1;
	double frac, newFrac, pi, err = pow(10, -n);
	while (1) {
		newFrac = (double) 4*i/m;
		i *= -1;
		m += 2;
		pi += newFrac;
		if (fabs(frac-newFrac) < err) {
			break;
		}
		frac = newFrac;
	}
	return pi;
}

int main() {	
	int n;
    scanf("%d", &n);
    printf("%.10f\n", calPi(n));
	return 0;
}
