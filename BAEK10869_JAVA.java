import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK10869_JAVA {
    public static int plus(int a, int b){
        return a + b;
    }
    public static int minus(int a, int b){
        return a - b;
    }

    public static int multiply(int a, int b){
        return a * b;
    }

    public static int divide(int a, int b) {
        return a / b;
    }

    public static int mod (int a, int b){
        return a % b;
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        System.out.println(plus(A,B));
        System.out.println(minus(A,B));
        System.out.println(multiply(A,B));
        System.out.println(divide(A,B));
        System.out.println(mod(A,B));

        br.close();
    }
}
