import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] l = new int[n + 1];
        l[0] = 0;
        l[1] = 1;
        for (int i = 2; i <= n; i++) {
            l[i] = l[i - 1] + 1;
            for (int j = 1; j * j <= i; j++) {
                l[i] = Math.min(l[i], l[i - j * j] + 1); // j*j가 곱해지면 1개의 square가 추가되니까 +1
            }
        }
        System.out.println(l[n]);
    }
}
