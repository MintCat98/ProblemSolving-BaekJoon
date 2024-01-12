import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int v = Integer.parseInt(br.readLine());
        String w = br.readLine();
        int c = 0;
        for (int i = 0; i < v; i++) {
            if (w.charAt(i) == 65) {
                c++;
            } else {
                c--;
            }
        }
        if (c == 0) {
            System.out.println("Tie");
        } else if (c > 0) {
            System.out.println("A");
        } else {
            System.out.println("B");
        }
    }
}
