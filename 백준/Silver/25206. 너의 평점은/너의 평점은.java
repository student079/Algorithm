import java.io.*;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        HashMap<String, Double> hashMap = new HashMap<>(9);
        hashMap.put("A+", 4.5);
        hashMap.put("A0", 4.0);
        hashMap.put("B+", 3.5);
        hashMap.put("B0", 3.0);
        hashMap.put("C+", 2.5);
        hashMap.put("C0", 2.0);
        hashMap.put("D+", 1.5);
        hashMap.put("D0", 1.0);
        hashMap.put("F", 0.0);

        double total = 0;
        double sum = 0;
        for (int i = 0; i < 20; i++) {
            String[] arr = bufferedReader.readLine().split(" ");
            if (!arr[2].equals("P")) {
                double s = Double.parseDouble(arr[1]);
                total += s;
                sum += hashMap.get(arr[2])*s;
            }
        }

        bufferedWriter.write(String.valueOf(sum/total));

        bufferedWriter.close();
        bufferedReader.close();
    }
}
