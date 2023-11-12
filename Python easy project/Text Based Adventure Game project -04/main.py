userinput=input("Do you want to play this game? [yes/no]:")
if userinput=='yes':
    print("🤠Welcome to the game!🤠")
    userinput=input("Where do you want to go? [🌊chattogram/🌱kurigram]:")


# Chattogram zone.....

    if userinput=='chattogram':
        print("Here you can enjoy 34 tourists spot")
        userinput=input("Which place would be better?[Patenga/zoo]:")
        if userinput == "Patenga":
            print('Yes! You choose the best place in Chattogram 🌊')
            print("You Won🏅🏅🏅")
        elif userinput == 'zoo':
            print("No! Patenga is better than Zoo 🤕 /n Better Luck next time 🤞")



# Kurigram zone.......

    elif userinput == 'kurigram':
        print("Here you can enjoy 8 tourists spot")
        userinput = input("Which place would be better?[dharla/border]:")
        if userinput == 'dharla':
            print("yes! You choose the best place in Kurigram 🏞️")
            print("🥳--Enjoy--🥳")
        elif userinput == 'border':
            print('Dharla is better than Border area! ⭕')
            print('Better luck Next time!😥')
else:
    print("👾👾Ok! Game Closed..👾👾")