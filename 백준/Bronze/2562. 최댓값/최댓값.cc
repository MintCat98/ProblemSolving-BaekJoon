#include <stdio.h>

int main() {
	short* arr = new short[10];
	short max = 0, loc = 0;
	for (short i = 0; i < 9; i++) {
		scanf("%d", &arr[i]);
	}
	for (short i = 0; i < 9; i++) {
		if (arr[i] > max) {
			max = arr[i];
			loc = i + 1;
		}
	}
	printf("%d\n%d", max, loc);
	delete[] arr;
	return 0;
}