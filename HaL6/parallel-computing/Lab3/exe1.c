# include <stdio.h>
# include <time.h>
# include <omp.h>

int main() {
    int n, i;
    clock_t begin, end;
    scanf("%d", &n);
    begin = clock();
    long res = 1;
    # pragma omp parallel for shared(n) private(i) reduction(*:res)
        for (i = 2; i <= n; ++i) {
            res *= i;
        }
    printf("%ld\n", res);
    end = clock();
    double executionTime = (double) (end-begin)/CLOCKS_PER_SEC;
    printf("%f\n", executionTime);
    return 0;
}
