import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK2675_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            String str = st.nextToken().trim();
            char[] strArr = str.toCharArray();
            String ans = "";
            for (int k = 0; k < strArr.length; k++) {
                for (int j = 0; j < R; j++)
                    ans += strArr[k];
            }
            System.out.println(ans);

        }

        br.close();
    }
}
