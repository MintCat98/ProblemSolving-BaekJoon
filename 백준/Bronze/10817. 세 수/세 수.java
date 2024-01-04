import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> l = new ArrayList<>(3);
        for (int i=0; i<3;i++){
            l.add(Integer.parseInt(st.nextToken()));
        }
        l.sort(Comparator.naturalOrder());
        System.out.println(l.get(1));
    }
}