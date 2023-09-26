#include <stdio.h>

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	int* arr = new int[n] {0, };
	for (int i = 0; i < m; i++) {
		int s, e, k;
		scanf("%d%d%d", &s, &e, &k);
		for (int j = s - 1; j < e; j++) {
			arr[j] = k;
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	return 0;
}