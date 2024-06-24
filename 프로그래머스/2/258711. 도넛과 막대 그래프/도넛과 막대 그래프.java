// 생성된 정점 찾기
// 생성된 정점 -> 들어오는 간선 X 나가는 개수만큼 기존 도형 개수
// 도넛 -> 모든 정점이 들어오고 나가는 간선 하나씩
// 막대 -> 나가는 간선이 없는 정점 존재
// 8자 -> 1개의 정점을 제외하면 나가는 간선과 들어오는 정점이 하나씩 존재. 1개의 정점은 나가는 간선 2개와, 들어오는 간선 2개가 존재
// 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다. -> 생성된 정점의 나가는 개수 최소 2개

import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = new int[] {0,0,0,0};
        
        // 들어오고 나가는 간선 개수 카운트
        HashMap<Integer, int[]> edgeCnt = new HashMap<>();
        
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0], b = edges[i][1];
            
            if (!edgeCnt.containsKey(a)){
                edgeCnt.put(a, new int[] {0, 0});
            }
            if (!edgeCnt.containsKey(b)) {
                edgeCnt.put(b, new int[] {0, 0});
            }
            
            // {out, in}
            edgeCnt.get(a)[0] += 1;
            edgeCnt.get(b)[1] += 1;
        }
        
        for (int key : edgeCnt.keySet()) {
            
            // {out, in}
            int[] cnts = edgeCnt.get(key);
            
            // 들어오는 간선이 없고 나가는 간선이 2개 이상일때 생성된 정점
    		if(cnts[0] >= 2 && cnts[1] == 0 ) {
    			answer[0] = key;
                
    		// 들어오는 간선의 개수가 막대 그래프의 개수
    		}else if(cnts[0] == 0 && cnts[1] > 0) {
    			answer[2]++;
                
    		// 들어오는것 나가는것 각 2개 이상인 점의 개수는 8자 그래프의 개수
    		}else if(cnts[0] >= 2 && cnts[1] >= 2) {
    			answer[3]++;
    		}
        }
        
        // 생성된 정점의 나가는 간선의 수에서 막대와 8자를 제외한것이 도넛 그래프의 개수
        answer[1] = edgeCnt.get(answer[0])[0] - answer[2] - answer[3];
        
        return answer;
    }
}