import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK2884_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int hours = Integer.parseInt(st.nextToken());
        int minutes = Integer.parseInt(st.nextToken());

        minutes -= 45;
        if (minutes < 0) {
            hours -= 1;
            minutes = 60 + minutes;
            if (hours < 0)
                hours = 24 + hours;
        }

        System.out.printf("%d %d\n", hours, minutes);

        br.close();
    }
}
