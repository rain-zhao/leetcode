import java.util.HashMap;
import java.util.Map;

class Trie {

    private class TrieNode{
        Map<Character,TrieNode> children = new HashMap<>();
        boolean isEndOfWord = false;
    }

    TrieNode root = new TrieNode();

    /** Initialize your data structure here. */
    public Trie() {

    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode node = root;
        for(char c : word.toCharArray()){
            TrieNode children = node.children.get(c);
            if(children == null){
                children = new TrieNode();
                node.children.put(c,children);
            }
            node = children;
        }
        node.isEndOfWord = true;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = root;
        for(char c : word.toCharArray()){
            TrieNode children = node.children.get(c);
            if(children == null){
                return  false;
            }
            node = children;
        }
        return node.isEndOfWord;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for(char c : prefix.toCharArray()){
            TrieNode children = node.children.get(c);
            if(children == null){
                return  false;
            }
            node = children;
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */