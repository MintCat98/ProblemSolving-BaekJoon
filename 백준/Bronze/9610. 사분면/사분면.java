import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] qs = new int[5];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            if (x == 0) {
                qs[4]++;
            } else if (x > 0) {
                if (y == 0) {
                    qs[4]++;
                } else if (y > 0) {
                    qs[0]++;
                } else {
                    qs[3]++;
                }
            } else {
                if (y == 0) {
                    qs[4]++;
                } else if (y > 0) {
                    qs[1]++;
                } else {
                    qs[2]++;
                }
            }
        }
        for (int i = 0; i < 4; i++) {
            System.out.println(String.format("Q%d: %d", i + 1, qs[i]));
        }
        System.out.println("AXIS: " + qs[4]);
    }
}
