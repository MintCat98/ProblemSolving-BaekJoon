import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            float a = Float.parseFloat(st.nextToken());
            String o = "";
            while (true) {
                try {
                    o = st.nextToken();
                } catch (Exception e) {
                    break;
                }
                switch (o) {
                    case "@":
                        a *= 3;
                        break;
                    case "%":
                        a += 5;
                        break;
                    case "#":
                        a -= 7;
                        break;
                }
            }
            System.out.printf("%.2f\n", a);
        }
    }
}
