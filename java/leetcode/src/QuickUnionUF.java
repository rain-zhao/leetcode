public class QuickUnionUF {
    private int[] roots;

    public QuickUnionUF(int N) {
        roots = new int[N];
        for (int i = 0; i < N; i++) {
            roots[i]=i;
        }
    }

    private int findRoot(int i) {
        int root = i;
        while(root != roots[root]){
            root = roots[root];
        }
        while(roots[i] != root){
            int tmp = roots[i];
            roots[i] = root;
            i = tmp;
        }

        return root;
    }

    public boolean connected(int p, int q) {
        return findRoot(p)==findRoot(q);
    }

    public void union(int p, int q) {
        int proot = findRoot(p);
        int qroot = findRoot(q);
        roots[proot] = qroot;
    }
}
