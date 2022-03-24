#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <omp.h>

//char characters[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
char characters[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
size_t numOfCrts = sizeof(characters)/sizeof(characters[0]);
char password[100];
volatile bool flag = false;

void findPassword(int maxNumOfChars, char pre[]) {
	if (maxNumOfChars == 0) {
		return;
	}
	# pragma omp parallel for shared(flag)
	for (int i = 0; i < numOfCrts; ++i) {
		if (flag) {
			continue;
		}
		char prd[100] = "";
		strcpy(prd, pre);
		strncat(prd, &characters[i], 1);
		//printf("%s\n", prd);
		if (strcmp(password, prd) == 0) {
			printf("Your password is %s.\n", prd);
			flag = true;
		}
		findPassword(maxNumOfChars-1, prd);
	}
}

int main() {
	int maxLength = 15;
	printf("Enter your password (max length: %d; 0-9): ", maxLength);
	scanf("%s", password);
	clock_t startTime = clock();
	findPassword(maxLength, "");
	clock_t finishTime = clock();
	printf("Execution time: %f seconds.", (double) (finishTime-startTime)/CLOCKS_PER_SEC);
	return 0;
}
