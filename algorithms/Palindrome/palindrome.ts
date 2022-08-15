function isPalindrome(x: number): boolean {
    let strX = x.toString();
    return (strX == strX.split("").reverse().join(""));
};

console.log(isPalindrome(1211));