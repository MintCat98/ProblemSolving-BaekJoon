import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Long> hp = new PriorityQueue<>();
        PriorityQueue<Long> hm = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            long x = Long.parseLong(br.readLine());
            if (x == 0) {
                if (hp.isEmpty() && hm.isEmpty()) {
                    System.out.println(0);
                } else {
                    long p = (hp.isEmpty()) ? 0 : hp.peek();
                    long m = (hm.isEmpty()) ? 0 : hm.peek();
                    if (p == 0) {
                        System.out.println(hm.remove());
                    } else if (m == 0) {
                        System.out.println(hp.remove());
                    } else if (p >= -m) {
                        System.out.println(hm.remove());
                    } else {
                        System.out.println(hp.remove());
                    }
                }
            } else if (x > 0) {
                hp.add(x);
            } else {
                hm.add(x);
            }
        }
    }
}
