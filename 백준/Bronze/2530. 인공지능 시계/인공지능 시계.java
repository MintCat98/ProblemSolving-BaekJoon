import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int[] time = new int[3]; // hhMMss
        for (int i = 0; i < 3; i++) {
            time[i] = Integer.parseInt(st.nextToken());
        }

        int[] adds = new int[3]; // hhMMss
        adds[2] = n % 60;
        adds[1] = n / 60;
        if (adds[1] > 59) {
            adds[0] = adds[1] / 60;
            adds[1] %= 60;
        } else {
            adds[0] = 0;
        }

        time[2] += adds[2];
        if (time[2] > 59) {
            time[1] += time[2] / 60 + adds[1];
            time[2] %= 60;
        } else {
            time[1] += adds[1];
        }
        if (time[1] > 59) {
            time[0] += time[2] / 60 + adds[0] + 1;
            time[1] %= 60;
        } else {
            time[0] += adds[0];
        }
        time[0] %= 24;

        System.out.println(time[0]+" "+time[1]+" "+time[2]);
    }
}
