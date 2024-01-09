import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int cal(String eq) {
        ArrayList<String> l = new ArrayList<>(Arrays.asList(eq.split("\\+")));
        int temp = 0;
        for (String s : l) {
            temp += Integer.parseInt(s);
        }
        return temp;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer eq = new StringTokenizer(br.readLine(), "-", true);
        int n = eq.countTokens();
        int sum = 0;
        String str;
        for (int i = 0; i < n; i++) {
            try {
                str = eq.nextToken();
                if (str.equals("-")) {
                    sum -= cal(eq.nextToken());
                } else {
                    sum += cal(str);
                }
            } catch (Exception e) {}
        }
        System.out.println(sum);
    }
}
