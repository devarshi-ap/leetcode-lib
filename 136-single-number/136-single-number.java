class Solution {
    public static int singleNumber(int[] nums) {
        Map<Integer, Integer> mapNums = new HashMap<>();

        for (int n: nums) {
            if (mapNums.containsKey(n)) {
                mapNums.replace(n, mapNums.get(n) + 1);
            } else {
                mapNums.put(n, 1);
            }
        }
        int single = 0;
        for (int i : mapNums.keySet()) {
            if (mapNums.get(i) == 1) {
                single = i;
                break;
            }
        }
        return single;
    }
}