import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] l = new int[3][2];
        int ax, ay;
        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            l[i][0] = Integer.parseInt(st.nextToken());
            l[i][1] = Integer.parseInt(st.nextToken());
        }
        // x 비교
        if (l[0][0] == l[1][0]) {
            ax = l[2][0];
        } else if (l[0][0] == l[2][0]) {
            ax = l[1][0];
        } else {
            ax = l[0][0];
        }
        // y 비교
        if (l[0][1] == l[1][1]) {
            ay = l[2][1];
        } else if (l[0][1] == l[2][1]) {
            ay = l[1][1];
        } else {
            ay = l[0][1];
        }
        System.out.println(ax + " " + ay);
    }
}
