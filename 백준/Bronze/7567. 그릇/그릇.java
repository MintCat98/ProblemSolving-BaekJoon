import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int h = 10;
        for (int i = 1; i < s.length(); i++) {
            if (s.substring(i - 1, i).equals(s.substring(i, i + 1))) {
                h += 5;
            } else {
                h += 10;
            }
        }
        System.out.println(h);
    }
}
