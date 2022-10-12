class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> tripletsList = new ArrayList<List<Integer>>();  
        Set<List<Integer>> uniques = new HashSet<List<Integer>>();

        Arrays.sort(nums);
        
        for (int i=0; i<nums.length; i++) {
            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    uniques.add(Arrays.asList(nums[i], nums[j], nums[k]));
                }
                if (sum > 0) {
                    k--;
                } else {
                    j++;
                }
            }
        }

        tripletsList.addAll(uniques);
        return tripletsList;
    }
}