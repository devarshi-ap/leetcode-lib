class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] answer = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            int count = 0;
            for (int j=0; j<nums.length; j++) {
                count += (nums[i] > nums[j]) ? 1 : 0;
            }
            answer[i] = count;
        }
        return answer;
    }
}