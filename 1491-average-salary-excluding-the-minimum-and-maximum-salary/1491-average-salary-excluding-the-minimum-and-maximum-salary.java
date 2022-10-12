class Solution {
    public static double average(int[] salary) {
        Arrays.sort(salary);
        int sum=0, count=salary.length-2;
        for (int i=1; i<salary.length-1; i++) {
            sum += salary[i];
        }
        return (double) sum/count;
    }
}