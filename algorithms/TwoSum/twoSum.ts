function twoSum(nums: number[], target: number): number[] {
    for (let i=0; i<nums.length-1; i++) {
        for (let k=i+1; k<nums.length; k++) {
            if (nums[i] + nums[k] == target) {
                return [i, k]
            }
        }
    }
    return []
};

console.log(twoSum([2, 7, 9, 1], 11)); // [0, 2]