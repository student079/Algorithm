import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK10926_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ID = br.readLine();

        ID += "??!";
        System.out.println(ID);

        br.close();
    }
}
