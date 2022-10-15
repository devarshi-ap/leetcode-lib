class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;
        String[] jArr = jewels.split("");
        String[] sArr = stones.split("");

        for (int i=0; i<jArr.length; i++) {
            String jewel = jArr[i];
            for (int j=0; j<sArr.length; j++) {
                count += (sArr[j].equals(jewel)) ? 1 : 0;
            }
        }
        return count;
    }
}