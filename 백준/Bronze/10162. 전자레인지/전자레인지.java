import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        if (t % 10 != 0){
            System.out.println(-1);
            return;
        }
        int[] l = new int[3];
        int[] b = {300, 60, 10};
        for (int i = 0; i < 3; i++) {
            l[i] += t / b[i];
            t %= b[i];
        }
        System.out.println(l[0] + " " + l[1] + " " + l[2]);
    }
}
