# code start here.....
import random
dicerolling=True
while dicerolling:
    print(random.randrange(1,6))
    userinput=input("⚔️ Do you want to Roll again  [y/n] 🎲 :")
    if userinput == 'y':
        continue
    elif userinput == "n":
        print("☠️ Game over ☠️")
        break

    else:
        continue

# code End........

