import org.junit.jupiter.api.Test;

import java.util.*;

public class Task212 {

    TrieNode root = new TrieNode();

    int lx = 0;
    int ly = 0;

    Set<String> res = new HashSet<>();

    public List<String> findWords(char[][] board, String[] words) {

        //pre process
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            TrieNode node = root;
            for (char c:word.toCharArray()){
                int num = c-'a';
                if(node.children[num] == null){
                    node.children[num] = new TrieNode();
                }
                node = node.children[num];
            }
            node.isEndOfWord = true;
        }

        lx = board.length;
        ly = board[0].length;

        for (int i = 0; i < lx; i++) {
            for (int j = 0; j < ly; j++) {
                dfs(board, root, i,j,"");
            }
        }


        return new ArrayList<>(res);
    }

    void dfs(char[][] board, TrieNode node, int x, int y,String result){

        char c = board[x][y];
        if(c == '#'){
            return;
        }
        TrieNode child = node.children[c-'a'];

        if(child == null){
            return;
        }
        result+=c;
        if(child.isEndOfWord){
            res.add(result);
        }
        board[x][y]='#';

        if(x>0){
            dfs(board,child,x-1,y,result);
        }
        if(x< lx-1){
            dfs(board,child,x+1,y,result);
        }
        if(y>0){
            dfs(board,child, x,y-1,result);
        }
        if(y< ly-1){
            dfs(board,child, x,y+1,result);
        }

        board[x][y]=c;

    }

    @Test
    void test(){
        char[][] board ={{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        String[] words = new String[]{"oath","pea","eat","rain"};

        System.out.println(findWords(board,words));
    }

}
