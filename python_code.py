def isPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1

    
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True

s=input("Enter the string:")

if isPalindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
    

