class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for (int i=left; i<=right; i++) if (selfDivides(i)) ans.add(i);
        return ans;
    }

    public static boolean selfDivides(int num) {
        int x = num;
        while (num > 0) {
            int d = num % 10;
            System.out.println(num + " " + d);
            if (d == 0 || x % d != 0) return false;
            num /= 10;
        }
        return true;
    }
}