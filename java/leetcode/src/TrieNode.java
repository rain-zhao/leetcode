import java.util.HashMap;
import java.util.Map;

class TrieNode{
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord = false;
}