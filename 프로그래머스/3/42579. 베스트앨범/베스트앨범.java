// 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범

import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Comparator;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        int N = genres.length;
        HashMap<String, Integer> genreMapCount = new HashMap<String, Integer>();
        HashMap<String, ArrayList<int[]>> genreMapNumAndCount = new HashMap<>();
        
        for (int i = 0; i < N ; i++) {
            String genre = genres[i];
            int count = plays[i];
            
            genreMapCount.put(genre, genreMapCount.getOrDefault(genre, 0) + count);
            ArrayList<int[]> list = genreMapNumAndCount.getOrDefault(genre, new ArrayList<>());
            list.add(new int[]{i, count});
            genreMapNumAndCount.put(genre, list);
        }
        
        // genreMapCount count높은 장르 순으로 키 정렬
        List<String> genreKeySet = new ArrayList<>(genreMapCount.keySet());
        
        genreKeySet.sort(Comparator.comparingInt(key -> genreMapCount.get(key)).reversed());
        
        // 키 따라가면서 genreMapNumAndCount 정렬 해서 최대 두개 번호 넣기
        for (String key : genreKeySet) {
            List<int[]> songs = genreMapNumAndCount.get(key);
            
            songs.sort(Comparator.comparingInt((int[] o) -> o[1]).reversed());
            int size = Integer.min(songs.size(), 2);
            for (int i = 0; i < size; i++) {
                answer.add(songs.get(i)[0]);
            }
        }
        
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}