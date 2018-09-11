years_str = input("Years: ") # do not change this line
years_int = int(years_str)

totalsec_int = (years_int * 31536000)
birth_int = totalsec_int / 7
death_int = totalsec_int / 13
immigrant_int = totalsec_int / 35

old_pop = int(307357870)


new_population = old_pop + birth_int - death_int + immigrant_int
print("New population after", years_int, " years is ", int(new_population)) # do not change this line

