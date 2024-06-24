// 두사람이 주고 받은 기록이 있다 -> 더 많으 ㄴ선물을 준 사람이 다음달에 선물을 하나 받음
// 하나도 없거나 같다 -> 선물지수가 큰 사람이 받음
// 선물지수 = 준 선물의 수 - 받은 선물의 수
// 선물지수도 같다면 아무것도 안함
// 가장 많은 선물을 받을 친구의 받을 선물 수 반환

import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        
        // 2차원 배열로 기록
        // map으로 index, 이름 매치
        int friendsLength = friends.length;
        int[] answer = new int[friendsLength+1];
        HashMap<String, Integer> name2Idx = new HashMap<>();
        int[][] gs = new int[friendsLength+1][friendsLength+1];
        
        for (int i = 0; i < friendsLength; i++) {
            name2Idx.put(friends[i], i+1);
        }
        
        // 가로 합 = 선물 지수
        for (int i = 0; i < gifts.length; i++) {
            String[] ts = gifts[i].split(" ");
            int toIdx = name2Idx.get(ts[0]), fromIdx = name2Idx.get(ts[1]);
            gs[toIdx][fromIdx]+=1;
            gs[fromIdx][toIdx]-=1;
        }
        
        // 다음달 예측
        for (int i = 0; i < friendsLength; i++) {
            for (int j = i+1; j < friendsLength; j++) {
                int a = name2Idx.get(friends[i]);
                int b = name2Idx.get(friends[j]);
                
                if (a == b) continue;
                    
                if (gs[a][b] > gs[b][a]) {
                    answer[a]+=1;
                } else if (gs[b][a] > gs[a][b]) {
                    answer[b]+=1;
                }else {
                    // 선물지수 비교
                    int aSum = 0;
                    for (int k = 1; k < friendsLength + 1; k++) {
                        aSum += gs[a][k];
                    }
                    int bSum = 0;
                    for (int k = 1; k < friendsLength + 1; k++) {
                        bSum += gs[b][k];
                    }
                    
                    if (aSum > bSum) {
                        answer[a]+=1;
                    } else if (bSum > aSum) {
                        answer[b]+=1;
                    }
                }
                
                // 주고받은 선물기록 비교
                
            }
            
        }
        
//         for (int i = 0; i < friendsLength+1; i++) {
//             for (int j = 0; j < friendsLength+1; j++)
//                 System.out.print(gs[i][j]);
//             System.out.println();
//         }
        
        // 최대값 반환
        int maxValue = 0;
        for (int i = 1; i < friendsLength + 1; i++) {
            // System.out.print(answer[i]);
            if (answer[i] > maxValue)
                maxValue = answer[i];
        }
            
        return maxValue;
    }
}