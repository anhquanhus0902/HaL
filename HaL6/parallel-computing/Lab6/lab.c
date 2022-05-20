#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void multiplyTwoMatrix(int rowA, int colA, int rowB, int colB, int A[rowA][colA], int B[rowB][colB]) {
	int resMatrix[rowA][colB];
	for (int i = 0; i < rowA; ++i) {
		for (int j = 0; j < colB; ++j) {
			int res = 0;
			for (int k = 0; k < rowB; ++k) {
				res += A[i][k]*B[k][j];
			}
			resMatrix[i][j] = res;
		}
	}
	printf("result\n");
	for (int i = 0; i < rowA; ++i) {
		for (int j = 0; j < colB; ++j) {
			printf("%d ", resMatrix[i][j]);
		}
		printf("\n");
	}
}

int main() {

	// Generate 2 matrix randomly
	int se, sed, rowA, colA, rowB, colB;
	se = 10;
	sed = 74;
	rowA = rand()%se;
	colA = rand()%se;
	rowB = colA;
	colB = rand()%se;
	
	int A[rowA][colA];
	printf("matrix A\n");
	for (int i = 0; i < rowA; ++i) {
		for (int j = 0; j < colA; ++j) {
			A[i][j] = rand()%sed;
			printf("%d ", A[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	
	int B[rowB][colB];
	printf("matrix B\n");
	for (int i = 0; i < rowB; ++i) {
		for (int j = 0; j < colB; ++j) {
			B[i][j] = rand()%sed;
			printf("%d ", B[i][j]);
		}
		printf("\n");
	}
	printf("\n");	
	multiplyTwoMatrix(rowA, colA, rowB, colB, A, B);
	return 0;
}
