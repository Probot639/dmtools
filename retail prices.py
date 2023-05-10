# Write a way to resell magic and mundane items
import random

random.randint(0, 10)
print()
# comment
# Take spell level, calculate price,
# take item level, calculate price
# calculate price that it can be marked up to
# Sell at a set percent lower than that
def get_number():
    while True:
        try:
            number = int(input("Enter a number between 0 and 12: "))
            if number < 0 or number > 12:
                print("Number must be between 0 and 12.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 12.")


def check_validity():
  while True:
    lvl = input("Enter the spell level you wish to enchant with: ")
    if lvl.isdigit():
      return int(lvl)
    else:
      print(
        "This is not a level number. Please enter a real level number or the Wizarding Council will have your hide."
      )

# Size is scale, material is like stone, wood, normal metal, precious metal, etc., wotcOverride is if theres existing $$
# Materials: (0)Biological (wood, leather, fur), (1)Rocks (non-metals), (2)Non-precious metals, (3)Precious metals, Gems(4)
def findmundanecost(size, material, wotcOverride):
    baseprice = 1
    if (material == 0):
        baseprice += 20
    elif (material == 1):
        baseprice += 10
    elif (material == 2):
        baseprice += (30 * size)
    elif (material == 3):
        baseprice += (50 * size)
    elif (material == 4):
        baseprice += (150 * size)
    else:
        pass
    #if (wotcOverride != 0):
    #    baseprice = wotcOverride
    print(f"Size is {size}, material is {material}, and wotcOverride is {wotcOverride}")
    print(baseprice)
    return baseprice


# Example usage:
numberfromvalid = check_validity()
itemcost = input("How costly is the item? ")
print(f"The level is: {numberfromvalid}\nThe cost is: {itemcost}")
chooseSize = input(f"choose your size: \n(1): Size of a ring, pebble, coin, or some jewelry\n(2): size of a wand, an orb, or a small magical figurine\n(3) Size of small weapons, armor, or a shield\n(4) Size of larger weapons, larger armor pieces, and large shields\n(5) Size of a trap, or a portal or barrier. Things you don't carry, but are easy enough to manuver around\n(6) Size of such things as towering structures over the landscape, or giant contructs\n")
chooseMaterial = input("(0): Biological (wood, leather, fur)\n(1): Rocks (non-metals)\n(2): Non-precious metal\n(3): Precious metals\n(4): Gems\n")
chooseWOTC = input(f"Put a {0} here unless you have a price intended, in which case why u doing this?\n")
findmundanecost(1,1,0)

print(chooseSize,chooseMaterial,chooseWOTC)
findmundanecost(chooseSize,chooseMaterial,chooseWOTC)