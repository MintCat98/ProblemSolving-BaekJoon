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
            ArrayList<Long> d = new ArrayList<>(Arrays.asList(1L, 1L, 1L, 2L, 2L));
            if (n<6){
                System.out.println(d.get(n-1));
            } else {
                for(int j = 5; j < n; j++) {
                    d.add(j, d.get(j-1)+d.get(j-5));
                }
                System.out.println(d.get(n-1));
            }
        }
    }
}
