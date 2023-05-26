import java.io.*;
import java.util.StringTokenizer;

public class BAEK10951_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        String com;

        while ((com = br.readLine()) != null) {
            st = new StringTokenizer(com);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            bw.write((a + b) + "\n");
        }

        br.close();

        bw.flush();
        bw.close();
    }
}
