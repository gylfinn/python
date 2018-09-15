month = input("Month: ")
day = int(input("Day: "))

month = month.lower()
month = month.capitalize()

month_and_day = month + " " + str(day)




if month_and_day == "January 1":
    print("New year's day")

elif month_and_day == "June 17":
    print("National holiday")
    
elif month_and_day == "December 25":
    print("Christmas day")
    
else:
    print("Not a holiday")

