import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> lst = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            TreeSet<Integer> s = new TreeSet<>();
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            s.add(a);
            s.add(b);
            s.add(c);
            int l = s.size();
            if (l == 1) {
                lst.add(10000 + a * 1000);
            } else if (l == 3) {
                lst.add(s.last() * 100);
            } else {
                int d;
                if (a == b) {
                    d = a;
                } else if (a == c) {
                    d = a;
                } else {
                    d = b;
                }
                lst.add(1000 + d * 100);
            }
        }
        System.out.println(Collections.max(lst));
    }
}
