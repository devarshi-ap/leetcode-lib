class Solution {
    public int numberOfSteps(int num) {
        int steps = 0;
        while (num != 0) {
            num -= (num % 2 == 0) ? (num * 0.5) : 1;
            System.out.println(num);
            steps++;
        }
        return steps;
    }
}