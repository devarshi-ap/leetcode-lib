class Solution {
    public String restoreString(String s, int[] indices) {
        char[] restored = new char[s.length()];
        for (int i=0; i<s.length(); i++) restored[indices[i]] = s.charAt(i);
        return new String(restored);
    }
}