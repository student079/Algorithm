import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BAEK2480_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> nums = new ArrayList<>();

        int same = 0;
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());

            if (nums.indexOf(num) < 0)
                nums.add(num);
            else
                same = num;
        }

        nums.sort(Comparator.naturalOrder());
        int numsSize = nums.size();
        if (numsSize == 3)
            System.out.println(nums.get(2) * 100);
        else if (numsSize == 2)
            System.out.println(same * 100 + 1000);
        else
            System.out.println(nums.get(0) * 1000 + 10000);


        br.close();

    }
}
