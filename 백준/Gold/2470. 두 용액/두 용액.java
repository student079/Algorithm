
import java.util.*;
import java.io.*;


//0에 가장 가까운 용액 만들기
//투포인터?
//N100,000
//-1,000,000,000 ~ 1,000,000,000 int로 가능
//객체 정렬도 한번 해보기
public class Main {

    static int N;
    static int[] drinks;
    static int minValue;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        drinks = new int[N];
        for (int i = 0; i < N; i++) {
            drinks[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(drinks);

        int left = 0;
        int right = N-1;
        minValue = Integer.MAX_VALUE;
        int[] answer = new int[2];

        while (left < right) {
            int s = drinks[left] + drinks[right];

            if (Math.abs(s) < minValue) {
                minValue = Math.abs(s);

                answer = new int[]{drinks[left], drinks[right]};

                if (s == 0) {
                    break;
                }
            }

            if (s < 0) {
                left++;
            } else {
                right--;
            }

        }

        System.out.println(answer[0] + " " + answer[1]);
    }
}
