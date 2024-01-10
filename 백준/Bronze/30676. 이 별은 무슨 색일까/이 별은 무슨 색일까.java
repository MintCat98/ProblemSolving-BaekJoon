import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (619 < n & n < 781) {
            System.out.println("Red");
        } else if (589 < n & n < 620) {
            System.out.println("Orange");
        } else if (569 < n & n < 590) {
            System.out.println("Yellow");
        } else if (494 < n & n < 570) {
            System.out.println("Green");
        } else if (449 < n & n < 495) {
            System.out.println("Blue");
        } else if (424 < n & n < 450) {
            System.out.println("Indigo");
        } else {
            System.out.println("Violet");
        }
    }
}
