import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BAEK10871_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        ArrayList<Integer> arrs = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()){
            int temp = Integer.parseInt(st.nextToken());
            if (X > temp)
                arrs.add(temp);
        }

        for (int temp : arrs)
            System.out.printf("%d ",temp);

        System.out.println();

        br.close();
    }
}
