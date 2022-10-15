class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] leftProd = new int[nums.length];
        int[] rightProd = new int[nums.length];

        int product = 1;
        
        // get left hand products
        for (int i=0; i<nums.length; i++) {
            leftProd[i] = product;
            product *= nums[i];
        }

        System.out.println(Arrays.toString(leftProd));

        // get right hand products
        product = 1;
        for (int i=nums.length-1; i>=0; i--) {
            rightProd[i] = product;
            product *= nums[i];
        }

        System.out.println(Arrays.toString(rightProd));

        // merge left and right hand product arrays (1-to-1)
        for (int i=0; i<nums.length; i++) {
            answer[i] = leftProd[i] * rightProd[i];
        }

        return answer;
    }
}