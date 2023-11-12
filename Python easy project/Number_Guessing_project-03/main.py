import random
random_year=random.randrange(2000,2006)
userinput=int(input("Guess My BirthYear:"))
if userinput > random_year:
    print(random_year)
    print("Too High")
elif random_year > userinput:
    print(random_year)
    print("Too Low")
else:
    print(random_year)
    print("Correct!")


