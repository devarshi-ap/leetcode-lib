class Solution {
    public static int removeDuplicates(int[] nums) {
        ArrayList<Integer> uniques = new ArrayList<Integer>();
        int count = 0;

        for (int x: nums) {
            if (!uniques.contains(x)) {
                uniques.add(x);
                nums[count] = x;
                count++;
            }
        }

        return uniques.size();
    }
}