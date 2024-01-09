import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> l = new ArrayList<>(Arrays.asList(1, 2));
        if (n < 3) {
            System.out.println(l.get(n - 1));
            return;
        }
        for (int i = 2; i < n; i++) {
            l.add((l.get(i - 1) + l.get(i - 2)) % 10007);
        }
        System.out.println(l.get(n - 1));
    }
}
