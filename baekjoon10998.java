import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon10998 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A,B;
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        System.out.println(A*B);

        br.close();
    }
}
