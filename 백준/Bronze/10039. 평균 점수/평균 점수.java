import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int s = 0;
        int t;
        for (int i = 0; i < 5; i++) {
            t = Integer.parseInt(br.readLine());
            if (t < 40) {
                t = 40;
            }
            s += t;
        }
        System.out.println(s / 5);
    }
}
