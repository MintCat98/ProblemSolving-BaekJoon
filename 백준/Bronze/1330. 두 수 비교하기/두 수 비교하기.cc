#include <stdio.h>
int main(void) {
	short a, b;
	scanf("%hd%hd", &a, &b);
	if (a > b) {
		printf(">");
	}
	else if (a < b) {
		printf("<");
	}
	else {
		printf("==");
	}
}