#!/usr/bin/env node

var judgePalindrome = function(s) {
    // return (s.split("").reverse().join("") == s);
    const len = s.length;
    for (let i = 0; i <= (len-i-1); i++) {
        if (s[i] !== s[len - i - 1]) {
            return false;
        }
    }
    return true;
};

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let maxStr = "";
    let maxLength = 0;
    let length = s.length;
    for (let i = 0; i + maxLength < length; i++) {
        for (let j = length-1; j >= i + maxLength; j--) {
            let tempStr = s.substr(i, j-i+1);
            if (s[i] == s[j] && judgePalindrome(tempStr)) {
                maxStr = tempStr;
                maxLength = j+1-i;
            }
        }
    }
    return maxStr;
};

let string1 = "cbbdbb";
let string2 = "a";
let string3 = "cbbd";
let string4 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
let string5 = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
let res = longestPalindrome(string5);
// let res = judgePalindrome(string3);
console.log("=============");
console.log(res);
