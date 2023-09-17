#include <stdio.h>
int main(void) {
	short h,m;
	scanf("%hd\n%hd", &h,&m);
	if (m - 45 < 0) {
		if (h - 1 < 0) {
			printf("23 %hd", m + 15);
		}
		else {
			printf("%hd %hd", h - 1, m + 15);
		}
	}
	else {
		printf("%hd %hd", h, m - 45);
	}
}