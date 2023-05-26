import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK2525_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int hours = Integer.parseInt(st.nextToken());
        int minutes = Integer.parseInt(st.nextToken());
        int time = Integer.parseInt(br.readLine());

        minutes += time;
        while (minutes >= 60) {
            minutes -= 60;
            hours += 1;
            if (hours >= 24)
                hours -= 24;
        }

        System.out.println(hours + " " + minutes);

        br.close();

    }
}
