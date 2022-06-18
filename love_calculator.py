"""
    Instruction:
        You are going to write a program that test the compatibility between two peoples.
        we are gong to use super scientific method recommended by BuzzFeed.
        
        To work out the love score between two people:
            -   Take both people's names and check for the number of times the letter in the word TRUE occurs.
                Then check for the number of times the letters is in the word LOVE occurs. 
                Then combine these to number to make 2 digit number.
                
                name 1 = aRianna REbOLini
                name 2  = channing TaTUm
                
                    T[2]     L[1]
                    R[2]     O[1]
                    U[1]     V[0]
                    E[1]     E[1]
                ---------------------
                    [6]        [3]  => 63%
                    
        - for love score less than 10 and greater than 90, the msg should be :
            Your score is X and you go together like coke and mentos
        - for love score between 40 and 50, the msg should be :
            Your score is X and you are alright together.
        - Otherwise, the msg will just be their score. e.g.:
            Your score is X.
"""
print("----------- LOVE CALCULATOR -----------")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_string = name1 + name2

# TRUE
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true_count = str(t + r + u + e)

# LOVE
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love_count = str(l + o + v + e)

love_percentage  = int(true_count + love_count)

if (love_percentage <= 10) or (love_percentage >= 90):
    print(f"Your score is {love_percentage}%, you goes like coke and mentos.")
elif (love_percentage >= 40) and (love_percentage <= 50):
    print(f"Your score is {love_percentage} and you are alright together!")
else:
    print(f"Your score is {love_percentage}.")