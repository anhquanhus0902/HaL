#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
	int pid;
	if ((pid = fork()) == 0){
		printf("hello from the child\n");
	}
	else{
		printf("hello from the parent\n");
	}
	return 0;
}
