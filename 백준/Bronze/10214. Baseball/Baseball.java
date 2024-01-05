import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int ys = 0;
            int ks = 0;
            for (int j = 0; j < 9; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                ys += Integer.parseInt(st.nextToken());
                ks += Integer.parseInt(st.nextToken());
            }
            if (ys > ks) {
                System.out.println("Yonsei");
            } else if (ys < ks) {
                System.out.println("Korea");
            } else {
                System.out.println("Draw");
            }
        }
    }
}
