
string = input("Setning: ")



for char in string:
        if char == "," or char == "." or char == '"' or char == "'" or char == "-" or char == "!":
            string = string.replace(char,"")

print(string)