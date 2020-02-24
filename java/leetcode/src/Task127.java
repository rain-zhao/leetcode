import org.junit.jupiter.api.Test;

import java.util.*;

public class Task127 {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        int size = wordList.size();
        int[] cnts = new int[size+1];

        Arrays.fill(cnts,Integer.MAX_VALUE);

        cnts[wordList.size()] = 1;

        wordList.add(beginWord);
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(size);

        while(!queue.isEmpty()){
            int idx = queue.poll();
            String word = wordList.get(idx);
            int cnt = cnts[idx];
            for (int i = 0; i < size; i++) {
                String change = wordList.get(i);
                if(similar(word,change) && cnts[i] == Integer.MAX_VALUE){
                    cnts[i] = cnt+1;
                    if(change.equals(endWord)){
                        return cnts[i];
                    }
                    queue.offer(i);
                }
            }

        }


        return 0;
    }


    boolean similar(String word,String change){
        int diff = 0;
        for (int i = 0; i < word.length(); i++) {
            if(word.charAt(i) != change.charAt(i)){
                ++diff;
                if(diff > 1){
                    return false;
                }
            }
        }
        return true;
    }

    @Test
    void test(){
        String beginWord = "hit";
        String endWord = "cog";
        List<String> wordList = new ArrayList<>(Arrays.asList("hot","dot","dog","lot","log","cog"));
        System.out.println(ladderLength(beginWord,endWord,wordList));

    }
}
