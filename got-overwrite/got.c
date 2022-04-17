#include <stdio.h>

void username(){
 while(1) {
	char username[300];
        fgets(username,sizeof(username),stdin);
        printf(username);
	puts("");
}}


int main() {
	username();
	return 0;
}
