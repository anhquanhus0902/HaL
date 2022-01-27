#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
	int pid;
	pid = fork();
	if (pid == 0){
		fork();
		printf("medium\n");
		fork();
		fork();
		printf("small\n");
	}
	else{
		printf("big\n");
	}
	return 0;
}
