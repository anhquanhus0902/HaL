int write_data(char* buf, size_t len) {
	int fileExist, fd;
	int turn = 0;
	while(1) {
		char* file = "output.dat";
		fileExist = check_file_existence(file);
		if (!fileExist) {
			fd = open(file, O_CREAT);
			while (turn);
			write(fd, buf, len);
			turn = 1;
		}
	}
}