#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0
#define DELAY	sleep(rand() % 4)

int account; // tai khoan ngan hang
int turn;
int interest[2];

void enter_region(int pid) {
	int other;
	other = 1 - pid;
	interest[pid] = TRUE;
	turn = pid;
	while (turn == pid && interest[other] == TRUE);
}

void leave_region(int pid) {
	interest[pid] = FALSE;
}

void *chaGuiTien() {  // luot =0
	int x;
	while (TRUE) {
		enter_region(0); 
		int soTienGui = 2;
		x = account;
		DELAY;
		x += soTienGui;
		DELAY;
		account = x;
		DELAY;
		leave_region(0);
		printf("Bo: Tao da gui. Account=%d\n", account);
	}
}

void *conRutTien() { // luot =1
	int y;
	while (TRUE) {
		enter_region(1); 
		int soTienRut = 3;
		y = account;
		DELAY;
		y -= soTienRut;
		DELAY;
		if (y < 0){
			printf("Khong du tien\n");
		}
		else{
			account = y;
			DELAY;
			printf("Con ra rut. Account=%d\n", account);
		}
		leave_region(1); 
		DELAY;	
	}
}

void main() {
   pthread_t tid1, tid2;
   
   printf("Account=%d\n",account);
   pthread_create(&tid1, NULL, chaGuiTien, NULL);   
   pthread_create(&tid2, NULL, conRutTien, NULL);   
   
   pthread_join(tid1, NULL);  
   pthread_join(tid2, NULL);  
}
