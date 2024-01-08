import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            ArrayList<Integer> d = new ArrayList<>(Arrays.asList(1, 2, 4));
            if (n < 4) {
                System.out.println(d.get(n - 1));
            } else {
                for (int j = 3; j < n; j++) {
                    d.add(j, d.get(j - 3) + d.get(j - 2) + d.get(j - 1));
                }
                System.out.println(d.get(n-1));
            }
        }
    }
}
