class Solution {
    public int lengthOfLastWord(String s) {
        String[] chars = s.split(" ");
        return chars[chars.length-1].length();
    }
}