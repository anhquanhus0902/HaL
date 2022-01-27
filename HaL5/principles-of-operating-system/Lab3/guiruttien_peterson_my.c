#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<stdlib.h>

#define DELAY	sleep(rand()%4)
#define N		2

int account = 5;
int turn;
int interest[N];

void enter_region(int pid){
	int other = 1-pid;
	interest[pid] = 1;
	turn = pid;
	while (turn == pid && interest[other] == 1);
}

void leave_region(int pid){
	interest[pid] = 0;
}

void* chaGuiTien(void* tienGui){
	while (1){
		enter_region(0);
		int x;
		x = account;
		DELAY;
		x += *((int *) tienGui);
		DELAY;
		account = x;
		DELAY;
		printf("Bo da gui. Account=%d\n", account);
		leave_region(0);
	}
}

void* conRutTien(void* tienRut){
	while (1){
		enter_region(1);
		int y;
		y = account;
		DELAY;
		y -= *((int *) tienRut);
		DELAY;
		if (y < 0){
			printf("Khong du tien.\n");
		}
		else{
			account = y;
			DELAY;
			printf("Con ra rut. Account=%d\n", account);
		}
		leave_region(1);
	}	
}

int main(){
	pthread_t tid1, tid2;
	int tienGui = 2, tienRut = 3;
	printf("Account=%d\n", account);
	pthread_create(&tid1, NULL, chaGuiTien, (void*) &tienGui);
	pthread_create(&tid2, NULL, conRutTien, (void*) &tienRut);
	
	pthread_join(tid1, NULL);
	pthread_join(tid2, NULL);
	return 0;
}
