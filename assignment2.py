"""This program greets the user, and presents a menu for them to choose
from.
"""
import assignment1


def print_menu():
    """Print the menu."""
    print("")
    print("Main Menu:")
    print("1 - Print Average Particulate Concentration by Zip Code and Time")
    print("2 - Print Minimum Particulate Concentration by Zip Code and Time")
    print("3 - Print Maximum Particulate Concentration by Zip Code and Time")
    print("4 - Adjust Zip Code Filters")
    print("5 - Load Data")
    print("9 - Quit")


def menu():
    """Display the menu and allow the user to choose an option."""
    print_menu()
    user_input = input("What is your choice?")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a number")
    finally:
        print("Thank you!")


def main():
    """Display the menu and allow the user to choose an option."""
    menu()


if __name__ == "__main__":
    main()


"""
-----Valid Input-----
Please enter your name:Advait
Hi Advait, nice to meet you! I look forward to working with you.

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice?1
Thank you!

Process finished with exit code 0


-----Invalid Input-----
Please enter your name:Advait
Hi Advait, nice to meet you! I look forward to working with you.

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice?one
Please enter a number
Thank you!

Process finished with exit code 0
"""