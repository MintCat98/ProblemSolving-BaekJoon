import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] paper;
    static int[] wb = {0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // Init
        paper = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // Recursion
        solve(0, 0, n);
        System.out.println(wb[0]);
        System.out.println(wb[1]);
    }

    static void solve(int x0, int y0, int size) {
        // 시작점과 같은 색상으로 이루어진 정사각형이 나올때까지 반씩 잘라야함
        int color = paper[y0][x0];
        // Search
        boolean same = true;
        for (int y = y0; y < size + y0; y++) {
            for (int x = x0; x < size + x0; x++) {
                if (color != paper[y][x]) {
                    same = false;
                    break;
                }
            }
        }
        if (same) {
            // 찾아낸 뭉탱이가 색종이 1개로 취급됨
            wb[color]++;
        } else {
            // 현 상태에서 찾을 수 없다면 4등분
            size /= 2;
            solve(x0, y0, size); // 1번 영역
            solve(x0 + size, y0, size); // 2번 영역
            solve(x0, y0 + size, size); // 3번 영역
            solve(x0 + size, y0 + size, size); // 4번 영역
        }
    }
}
