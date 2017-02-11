#Given the string, check if it is a palindrome.

#Example

#For inputString = "aabaa", the output should be
#checkPalindrome(inputString) = true;
#For inputString = "abac", the output should be
#checkPalindrome(inputString) = false.
#Input/Output

#[time limit] 4000ms (py)
#[input] string inputString

#A non-empty string consisting of lowercase characters.

#Constraints:
#1 ? inputString.length ? 10.

#[output] boolean

#true if inputString is a palindrome, false otherwise.

def checkPalindrome(inputString):
    firstch = 0;
    lastch = len(inputString) - 1;
    palindrome = True;
    while (firstch < lastch) and (palindrome):
        if (inputString[firstch] != inputString[lastch]):
            palindrome = False;
        firstch += 1;
        lastch -= 1;
    return palindrome;

print checkPalindrome("aabaa");
print checkPalindrome("abac");
print checkPalindrome("abacaba");
print checkPalindrome("aabaa");
print checkPalindrome("a");
print checkPalindrome("aaaaaaaaaa");
print checkPalindrome("aaaaabbbbb");
print checkPalindrome("ab");

