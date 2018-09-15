# Your function definition goes here
def count_case(user_input):
    upper = 0
    lower = 0
    for char in user_input:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    return upper, lower   
    

user_input = input("Enter a string: ")
upper, lower = count_case(user_input)
# Call the function here

print("Upper case count: ", upper)
print("Lower case count: ", lower)