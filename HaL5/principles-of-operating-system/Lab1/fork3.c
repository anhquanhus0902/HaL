#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int val = 5;

int main(){
	pid_t pid;
	pid = fork();
	if (pid == 0){
		val += 15;
		printf("%d\n", val);
		return 0;
	}
	else if (pid > 0){
		wait(NULL);
		printf("PARENT: val = %d\n", val);
		return 0;
	}
}
