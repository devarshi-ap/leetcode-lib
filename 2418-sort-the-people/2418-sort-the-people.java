class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // #names == #heights
        int n = names.length;

        // init Integer[] array 0...n indices
        Integer[] idx = new Integer[n];
        for(int i=0; i<n; i++) idx[i] = i;
        
        // sort the indices w/ custom comparator
        Arrays.sort(idx, (a,b)->(heights[b]-heights[a]));
        
        // String[] array of names
        String[] ans = new String[n];
        for(int i=0; i<n; i++) ans[i] = names[idx[i]];
        return ans;
    }
}