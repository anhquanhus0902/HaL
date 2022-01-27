#define TRUE 	1
#define FALSE	0

int turn;

int write_data(char* buf, size_t len){
	int fileExist, fd;
	while(TRUE) {
		char* file = "output.dat";
		fileExist = check_file_existence(file);
		if (fileExist == FALSE){
			fd = open(file, O_CREAT);
			while (turn != 0);
			write(fd, buf, len);
			turn = 1;
		}
	}
}
