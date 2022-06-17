"""
    Write a program that works out whether if a giver year is leap year or not/
    Normal year has 365 days, while leap year has 366 days.
    
    - This is how you work out whether if a particular is a leap year or not :
        - On every year that is evenly divisible by 4   : 2020 / 4 = 505.0 [leap]   :   2100 / 4 = 525 [leap]
        - Except every year that is evenly divisible by 100 : 2020 /100 = 20.2 [leap]   :   2100 / 100 = 21 [not leap]
        - Unless the year is evenly divisible by 400    : 2020 / 400 = 5.5 [not leap]   :   2100 / 400 = 5.25 [not leap]
"""

"""
    FLOW CHART :
                        year
                        |
                        |
                        |
                    (year%4 == 0)
            -------------------
            |                 |
    (no, not Leap)          (yes, Leap)
                                |
                        (year%100 == 0)
                        ---------------
                        |             |
                (yes, not leap)     (no, leap)
                                        |
                                (year%400 == 0)
                                ---------------
                                |              |
                        (no, not leap)      (yes, leap)
                        
                        
"""

print("Let's find the leap year!")
year = int(input("Enter the year: "))
if (year % 4) == 0:
    # print('leap')
    if (year % 100) == 0:
        # print("not leap2")
        if (year % 400) == 0:
            # print('Leap')
            print(f"You entered year {year} and its a leap year.1")
        else:
            # print("not leap")
            print(f"You entered year {year} and its NOT a leap year.1")
    else:
        # print("leap")
        print(f"You entered year {year} and its a leap year.2")
else:
    print(f"You entered year {year} and its NOT a leap year.2")