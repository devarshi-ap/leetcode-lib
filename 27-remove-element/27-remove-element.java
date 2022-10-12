class Solution {
    public static int removeElement(int[] nums, int val) {
        int count = 0;
        for (int x: nums) {
            if (x != val) {
                nums[count] = x;
                count++;
            }
        }
        return count;
    }
}