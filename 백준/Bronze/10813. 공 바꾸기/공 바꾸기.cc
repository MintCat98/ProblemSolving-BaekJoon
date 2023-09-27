#include <stdio.h>

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		arr[i] = i+1;
	}
	int a, b, temp;
	for (int i = 0; i < m; i++) {
		scanf("%d%d", &a, &b);
		temp = arr[a - 1];
		arr[a - 1] = arr[b - 1];
		arr[b - 1] = temp;
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	delete[] arr;
	return 0;
}