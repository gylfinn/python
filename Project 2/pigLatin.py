word = str(input("Enter a word: "))

serhljodar_str = "aeiou"

while word not in ".":
    enginn_serhljodi = False
    word = word.lower()
    first_letter = word[0]

    for c in word:
        if c in serhljodar_str:
            enginn_serhljodi = True

    if enginn_serhljodi == False:
        word = word+"ay"
    elif first_letter in serhljodar_str:
        word = word+"yay"
    elif enginn_serhljodi == True:
        while first_letter not in serhljodar_str:
            word =  word[1:]+word[0]
            first_letter = word[0]
        word = word + "ay"
    

    print(word)
    word = str(input("Enter a word: "))


