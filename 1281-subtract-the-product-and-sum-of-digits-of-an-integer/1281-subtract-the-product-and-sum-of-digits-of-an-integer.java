class Solution {
    public int subtractProductAndSum(int n) {
        String[] digits = String.valueOf(n).split("");
        
        int sum=0, prod=1;
        
        for(String digit: digits) {
            int numDig = Integer.valueOf(digit);
            sum += numDig;
            prod *= numDig;
        }

        return prod-sum;
    }
}