"""This program greets the user, asks them to select a header, and presents a
menu for them to choose from. After they choose, the program lets them know if
their choice was okay.
"""


class DataSet:
    def __init__(self, header: str):
        self._data = None
        self._header = header


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


def menu(my_dataset: DataSet):
    """Display the menu and allow the user to choose an option."""
    while True:
        print(my_dataset._header)
        print_menu()
        user_input = input("What is your choice? ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Please enter a number only.")
            print("")
            continue
        if user_input == 9:
            print("Thank you")
            break
        elif (user_input == 1 or user_input == 2 or user_input == 3 or
                user_input == 4 or user_input == 5):
            print("This function isn't available yet. Pick another option!")
            print("")
        else:
            print("This option isn't listed in the menu! Try again.")
            print("")


def main():
    """Ask for user's name and header and execute menu code."""
    user_name = input("Please enter your name:")
    print("Hi " + user_name + ", nice to meet you! I look forward to working "
                              "with you.")
    header_input = input("Please enter a header: ")
    purple_air = DataSet(header_input)
    menu(purple_air)


if __name__ == "__main__":
    main()

"""
Please enter your name:Advait
Hi Advait, nice to meet you! I look forward to working with you.
Please enter a header: Clean Air, Clean Life
Clean Air, Clean Life

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice?1
This function isn't available yet. Pick another option!

Clean Air, Clean Life

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice?2
This function isn't available yet. Pick another option!

Clean Air, Clean Life

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice?3
This function isn't available yet. Pick another option!

Clean Air, Clean Life

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice?9
Thank you

Process finished with exit code 0
"""