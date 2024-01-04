import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int yes = 0;
        int temp;
        for (int i = 0; i < n; i++) {
            temp = Integer.parseInt(br.readLine());
            if (temp == 1) {
                yes += 1;
            } else {
                yes -= 1;
            }
        }
        if (yes > 0) {
            System.out.println("Junhee is cute!");
        } else {
            System.out.println("Junhee is not cute!");
        }
    }
}
