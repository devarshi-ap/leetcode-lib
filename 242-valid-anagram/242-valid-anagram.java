class Solution {
    public static void main(String[] args) {
        System.out.println(isAnagram("anagram", "nagxaram"));
    }

    public static boolean isAnagram(String s, String t) {
        if (s.length() == t.length()) {
            for (char c: s.toCharArray()) t = t.replaceFirst(String.valueOf(c), "");
            return (t.isEmpty()) ? true : false;
        } else {
            return false;
        }
    }
}