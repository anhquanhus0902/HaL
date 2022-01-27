#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

void main(){
	for (int i = 0; i < 2; i++){
		if (fork() != 0){
			printf("A\n");
		}
		else{
			fork();
			printf("B\n");
		}
		printf("C\n");
	}
}
