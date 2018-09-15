def isPalindrome(string):
   
    for char in string:
        if char == "," or char == "!" or char == "." or char == '"' or char == "'" or char == "-" or char == " ":
            string = string.replace(char,"")
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False    



string = input("Enter a string: ")

# call the function and print out the appropriate message

Palindrome = isPalindrome(string)

if Palindrome:
    print('"' + string + '"' + " is a palindrome.")
else:
    print('"' + string + '"' + " is not a palindrome.")