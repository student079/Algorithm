import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK10807_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] arrs = new int[N];

        for (int i = 0; i <N ;i++)
            arrs[i] = Integer.parseInt(st.nextToken());

        int v = Integer.parseInt(br.readLine());

        int sum = 0;
        for (int i = 0; i <N ;i++)
            if (arrs[i] == v)
                sum++;

        System.out.println(sum);

        br.close();

    }
}
