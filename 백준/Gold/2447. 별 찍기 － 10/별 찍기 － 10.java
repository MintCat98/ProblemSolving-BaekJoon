import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    // https://www.acmicpc.net/problem/2447
    static char[][] ss;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ss = new char[n][n];
        solve(0, 0, n, false);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(ss[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    static void solve(int x0, int y0, int size, boolean blank) {
        // 별 패턴 4번 반복 후, 공백 1개 추가
        if (blank) {
            for (int i = y0; i < y0 + size; i++) {
                for (int j = x0; j < x0 + size; j++) {
                    ss[j][i] = ' ';
                }
            }
            return;
        }

        if (size == 1) {
            ss[y0][x0] = '*';
            return;
        }
        
        // 9칸 구분
        int count = 0;
        int jump = size / 3; // 다음 칸으로 점프
        for (int i = y0; i < y0 + size; i += jump) {
            for (int j = x0; j < x0 + size; j += jump) {
                count++;
                if (count == 5) {
                    solve(j, i, jump, true);
                } else {
                    solve(j, i, jump, false);
                }
            }
        }
    }
}
