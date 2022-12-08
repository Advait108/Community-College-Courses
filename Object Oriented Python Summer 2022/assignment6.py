"""This program greets the user, asks them to select a header, and presents a
menu for them to choose from. After they choose, the program lets them know if
their choice was okay.
"""


def unit_test():
    """creating objects to induce self-made errors"""
    test1 = DataSet()
    try:
        test1._cross_table_statistics("94040", "Morning")
    except EmptyDatasetError:
        print("Method Raises EmptyDataSet Error: Pass")
    else:
        print("Method Does Not Raise EmptyDataSet Error: Fail")
    test1.load_default_data()
    try:
        test1._cross_table_statistics("94040", "Supper")
    except NoMatchingItems:
        print("Method Raises NoMatchingItems Error: Pass")
    else:
        print("Method Does Not Raise NoMatchingItems Error: Fail")
    try:
        test1._cross_table_statistics("94032", "Night")
    except NoMatchingItems:
        print("Method Raises NoMatchingItems Error: Pass")
    else:
        print("Method Does Not Raise NoMatchingItems Error: Fail")
    try:
        test1._cross_table_statistics("94040", "Night")
    except NoMatchingItems:
        print("Method Raises NoMatchingItems Error: Pass")
    else:
        print("Method Does Not Raise NoMatchingItems Error: Fail")
    if test1._cross_table_statistics("12345", "Morning") == (1.1, 1.1, 1.1):
        print("Single Matching Row Returns Correct Tuple: Pass")
    else:
        print("Single Matching Row Does Not Return Correct Tuple: Fail")
    if test1._cross_table_statistics("94040", "Morning") == (1.0, 2.0, 3.0):
        print("Multiple Matching Rows Return Correct Tuple: Pass")
    else:
        print("Multiple Matching Rows Does Not Return Correct Tuple: Fail")


class EmptyDatasetError(Exception):
    pass


class NoMatchingItems(Exception):
    pass


class DataSet:
    def __init__(self, header: str = ""):
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

    def load_default_data(self):
        """creating a list of tuples with sample data"""
        self._data = [("12345", "94022", "94040", "94022", "94040", "94022"),
                      ("Morning", "Morning", "Morning", "Midday", "Morning",
                       "Evening"), (1.1, 2.2, 3.0, 1.0, 1.0, 3.2)]

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        """checking to see if input zip code and time match sample data"""

        count = 0

        if self._data is None:
            count += 1
            raise EmptyDatasetError

        conc_list = [self._data[2][index] for index in
                     range(len(self._data[2])) if self._data[0][index] ==
                     descriptor_one and self._data[1][index] == descriptor_two]

        if len(conc_list) == 0:
            count += 1
            raise NoMatchingItems

        if count == 0:
            print(min(conc_list), sum(conc_list) / len(conc_list),
                  max(conc_list))
            return min(conc_list), sum(conc_list)/len(conc_list), \
                   max(conc_list)


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
    '''
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
    '''


if __name__ == "__main__":
    main()


"""
Method Raises EmptyDataSet Error: Pass
Method Raises NoMatchingItems Error: Pass
Method Raises NoMatchingItems Error: Pass
Method Raises NoMatchingItems Error: Pass
1.1 1.1 1.1
Single Matching Row Returns Correct Tuple: Pass
1.0 2.0 3.0
Multiple Matching Rows Return Correct Tuple: Pass

Process finished with exit code 0
"""