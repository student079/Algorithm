import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK18108_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int year = Integer.parseInt(br.readLine());

        System.out.printf("%d",year-(2541-1998));

        br.close();
    }
}
