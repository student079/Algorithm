// map에 종류별로 배열로 넣고
// +1 개해서 마지막에 -1(아예 안입는 경우)

import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        
        HashMap<String, Integer> mapClothes = new HashMap<String, Integer>();
        for (int i = 0; i < clothes.length ; i++) {
            String type = clothes[i][1];
            
            mapClothes.put(type, mapClothes.getOrDefault(type, 0) + 1);
        }
        
        int answer = 1;
        for (int value : mapClothes.values()) {
            answer *= (value+1);
        }
        
        return answer - 1;
    }
}