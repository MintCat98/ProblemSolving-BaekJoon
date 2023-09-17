#include <stdio.h>
int main(void) {
	short h, m, d;
	scanf("%hd %hd\n%hd", &h, &m, &d);
	if (d / 60 > 0) {
		h += d / 60;
		m += d % 60;
	}
	else {
		m += d;
	}
	if (m < 60) {
		if (h < 24) {
			printf("%hd %hd", h, m);
		}
		else {
			printf("%hd %hd", h - 24, m);
		}
	}
	else {
		if (h+1 < 24) {
			printf("%hd %hd", h + 1, m % 60);
		}
		else {
			printf("%hd %hd", h - 23, m % 60);
		}
	}
}