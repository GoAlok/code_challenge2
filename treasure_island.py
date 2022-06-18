from matplotlib.lines import Line2D


print("---------- Welcome to Treasure Island ----------")
print(' ')
print("Your mission is to find the treasure.")

line_1 = input('You\'re at a cross road where you want to go? Type "left" or "right"\n').lower()
if line_1 == "left":
    line_2 = input("After walking for hours on empty roads,you reached the ancient palace where \
it has three doors, 'red', 'blue', 'yellow'. To move further you have to make a difficult \
choice because ones you entered the door their is no way around. Type 'red' or 'blue' or 'yellow'\n").lower()
    if line_2 == "red":
        print("You entered the room of fire. You died because of sever burns.\n GAME OVER! \n")
    elif line_2 == "yellow":
        print("You entered the haunted room. Your body is possessed by demon, you failed to continue \
the treasure hunt.\n GAME OVER!\n")
    elif line_2 == "blue":
        print("You entered the room filled with ancient Golds, diamonds, rubies, jewelries . Yay! you \
found the largest treasure of history.\n YOU WIN!!! ")
    else:
        print("You entered non-existing door and reached to space where time has been stopped.\n GAME OVER!")
else:
    print("You fell in the hole which takes you to abandoned cave where hungry lion lives. \
So when you reached there 'The Lion' devour you.\n")
