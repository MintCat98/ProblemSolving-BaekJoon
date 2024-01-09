import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] l = new int[1000];
        l[0] = 1;
        l[1] = 3;
        for (int i = 2; i < n; i++) {
            l[i] = (l[i - 1] + 2 * l[i - 2]) % 10007;
        }
        System.out.println(l[n - 1]);
    }
}
