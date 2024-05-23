import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 길이 1000
        // Set에 넣기

        Set<String> set = new HashSet<>();
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String S = bufferedReader.readLine();
        int length = S.length();

        for (int i = 0; i < length; i++) {
            for (int j = i+1; j < length+1; j++) {
                set.add(S.substring(i,j));
            }
        }

        System.out.println(set.size());
    }

}
