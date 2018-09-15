def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True

string = input("Enter a string: ")

# call the function and print out the appropriate message

Palindrome = isPalindrome(string)

if Palindrome:
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")