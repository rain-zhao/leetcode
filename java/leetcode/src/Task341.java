import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Task341 {

    // This is the interface that allows for creating nested lists.
    // You should not implement it, or speculate about its implementation
    public interface NestedInteger {

        // @return true if this NestedInteger holds a single integer, rather than a nested list.
        public boolean isInteger();

        // @return the single integer that this NestedInteger holds, if it holds a single integer
        // Return null if this NestedInteger holds a nested list
        public Integer getInteger();

        // @return the nested list that this NestedInteger holds, if it holds a nested list
        // Return null if this NestedInteger holds a single integer
        public List<NestedInteger> getList();
    }

    public class NestedIterator implements Iterator<Integer> {

        List<Integer> list;
        Iterator<Integer> iter;

        public NestedIterator(List<NestedInteger> nestedList) {
            list = new ArrayList<>();
            for (NestedInteger nestedInteger : nestedList) {
                expand(nestedInteger);
            }
            iter = list.iterator();
        }

        @Override
        public Integer next() {
            return iter.next();
        }

        @Override
        public boolean hasNext() {
            return iter.hasNext();
        }

        void expand(NestedInteger nestedInteger) {
            if (nestedInteger.isInteger()) {
                list.add(nestedInteger.getInteger());
            } else {
                for (NestedInteger sub : nestedInteger.getList()) {
                    expand(sub);
                }
            }
        }
    }
}
