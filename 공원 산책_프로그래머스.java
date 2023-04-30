class Solution {
    public int[] solution(String[] park, String[] routes) {
        int x = 0;
        int y = 0;

        char[][] arr = new char[park.length][park[0].length()];

        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[i].length(); j++) {
                arr[i][j] = park[i].charAt(j);

                if (arr[i][j] == 'S') {
                    y = i;
                    x = j;
                }
            }
        }

        for(String st : routes){
            String way = st.split(" ")[0];
            int len = Integer.parseInt(st.split(" ")[1]);

            int nx = x;
            int ny = y;

            for(int i = 0; i < len; i++){
                switch (way) {
                    case "E":
                        nx++;
                        break;
                    case "W":
                        nx--;
                        break;
                    case "S":
                        ny++;
                        break;
                    case "N":
                        ny--;
                        break;
                }

                if (nx >= 0 && ny >= 0 && ny < arr.length && nx < arr[0].length) {
                    if(arr[ny][nx] == 'X'){
                        break;
                    }
                    if(i == len-1){
                        x = nx;
                        y = ny;
                    }
                }
            }
        }

        int[] answer = {y, x};
        return answer;
    }
}
