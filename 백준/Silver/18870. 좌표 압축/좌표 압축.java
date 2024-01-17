import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // List
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> orig = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            orig.add(Integer.parseInt(st.nextToken()));
        }
        // Sort + Unique
        TreeSet<Integer> set = new TreeSet<>(orig);
        // Map
        HashMap<Integer, Integer> map = new HashMap<>();
        int v = 0;
        for (int e : set) {
            map.put(e, v++);
        }
        StringBuilder sb = new StringBuilder();
        for (int e : orig) {
            sb.append(map.get(e) + " ");
        }
        System.out.println(sb);
    }
}
