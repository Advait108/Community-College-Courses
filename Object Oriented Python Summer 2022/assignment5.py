"""This program greets the user, asks them to select a header, and presents a
menu for them to choose from. After they choose, the program lets them know if
their choice was okay.
"""


class DataSet:
    def __init__(self, header: str=""):
        self._data = None
        self.header = header

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        if len(header) > 30:
            print("Please enter a shorter header")
            raise ValueError
        else:
            self._header = header


def unit_test():
    """ creating objects to test behavior of the __innit__() method"""
    test1 = DataSet()
    if test1.header == "":
        print("No parameter test PASSED- header is empty string")
    else:
        print("No parameter test FAILED")
    test2 = DataSet("Hello")
    if test2.header == "Hello":
        print("Valid parameter test PASSED- header is as expected")
    else:
        print("Valid parameter test FAILED")
    try:
        test3 = DataSet("12345678901234567890123456789000")
    except:
        print("Invalid parameter test PASSED- exception raised")
    else:
        print("Invalid parameter test FAILED- no exception raised")
    test2.header = "New Header"
    if test2.header == "New Header":
        print("Setter test PASSED- new header detected")
    else:
        print("Setter test FAILED- no new header detected")
    current_header = test2.header
    try:
        test2.header = "12345678901234567890123456789000"
    except:
        if current_header == test2.header:
            print("Invalid header setter test PASSED")
        else:
            print("Invalid header setter test FAILED")
    else:
        print("Invalid header setter test FAILED")


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
        print(my_dataset.header)
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
    """Ask for user's name and valid header and execute menu code."""
    unit_test()
    user_name = input("Please enter your name:")
    print("Hi " + user_name + ", nice to meet you! I look forward to working "
                              "with you.")
    purple_air = DataSet()
    while True:
        header_input = input("Please enter a header: ")
        try:
            purple_air.header = header_input
        except ValueError:
            continue
        else:
            break
    menu(purple_air)


if __name__ == "__main__":
    main()


"""
No parameter test PASSED- header is empty string
Valid parameter test PASSED- header is as expected
Please enter a shorter header
Invalid parameter test PASSED- exception raised
Setter test PASSED- new header detected
Please enter a shorter header
Invalid header setter test PASSED
Please enter your name:Advait
Hi Advait, nice to meet you! I look forward to working with you.
Please enter a header: hhhhhhhhhhhheeeeeeeeeeeeaaaaaaaaaadddddddddddeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
Please enter a shorter header
Please enter a header: is this okay now?
is this okay now?

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 1
This function isn't available yet. Pick another option!

is this okay now?

Main Menu:
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 9
Thank you

Process finished with exit code 0
"""
