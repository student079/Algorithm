import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> findByName = new HashMap<>();

        for (int i = 0; i < players.length; i++)
            findByName.put(players[i], i);

        for (String player : callings) {
            int place = findByName.get(player);

            String temp = players[place - 1];
            players[place - 1] = player;
            players[place] = temp;

            findByName.put(player, place - 1);
            findByName.put(temp, place);
        }

        return players;
    }
}

