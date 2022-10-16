class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> answer = new ArrayList<Boolean>();
        
        // init answer w/ false & get max
        int max=candies[0];
        for(int i=0; i<candies.length; i++) {
            answer.add(false);
            max = (candies[i] > max) ? candies[i] : max;
        }

        for(int i=0; i<candies.length; i++) {
            answer.set(i, (candies[i] + extraCandies >= max ) ? true : false);
        }

        return answer;
    }
}