class Solution {
    public int[] plusOne(int[] digits) {
        ArrayList<Integer> num = new ArrayList<>();
        
        if (digits.length == 1 && digits[0] == 9) {
            int[] arr = {1, 0};
            return arr;
        }

        // add one
        digits[digits.length-1] += 1;

        // transfer to arraylist
        for (int i=0; i<digits.length; i++) {
            num.add(digits[i]);
        }

        // traverse backwards, if 10 found, set to 0 and add 1 to prev (insert 1 to prev if first index) (do while list contains 10)
        while (num.contains(10)) {
            for (int i=num.size()-1; i>=0; i--) {
                System.out.println(num);
                if (num.get(i) == 10) {
                    if (i == 1 && num.get(0) == 9) {
                        num.set(i, 0);
                        num.set(0, 0);
                        num.add(0, 1);
                        int[] arr = num.stream().mapToInt(j -> j).toArray();
                        return arr;
                    }
                    num.set(i, 0);
                    num.set(i-1, num.get(i-1) + 1);
                }
            }
        }
        
        // System.out.println(num);
        int[] arr = num.stream().mapToInt(j -> j).toArray();
        return arr;
    }
}