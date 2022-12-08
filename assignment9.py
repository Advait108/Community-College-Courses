"""This program greets the user, asks them to select a header, and presents a
menu for them to choose from. After they choose, the program lets them know if
their choice was okay.

"""

from enum import Enum


def unit_test():
    my_dataset = DataSet()
    my_dataset.load_default_data()
    my_dataset.display_cross_table(Stats.MIN)
    my_dataset._zips["94022"] = False
    my_dataset.display_cross_table(Stats.MIN)
    my_dataset._zips["12345"] = False
    my_dataset._zips["94040"] = False
    my_dataset.display_cross_table(Stats.MIN)


class Stats(Enum):
    MIN = 0
    AVG = 1
    MAX = 2


class EmptyDatasetError(Exception):
    pass


class NoMatchingItems(Exception):
    pass


class DataSet:
    def __init__(self, header: str = ""):
        self._data = None
        self.header = header
        self._zips = {}
        self._times = []

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

    def _initialize_labels(self):
        """Sorting the data values into the correct places."""
        self._zips = {}
        day_times = set()
        for tup in self._data:
            for value in tup:
                try:
                    int(value)
                except:
                    day_times.add(value)
                else:
                    if not type(value) == float:
                        self._zips[value] = True

        self._times = list(day_times)

    def load_default_data(self):
        """creating a list of tuples with sample data"""
        self._data = [("12345", "94022", "94040", "94022", "94040", "94022"),
                      ("Morning", "Morning", "Morning", "Midday", "Morning",
                       "Evening"), (1.1, 2.2, 3.0, 1.0, 1.0, 3.2)]
        self._initialize_labels()

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):

        """checking to see if input zip code and time match sample data

        Keyword arguments:
            descriptor_one -- the label for the first category
            descriptor_two -- the label for the second category

        Returns a tuple of min, average, max from the matching rows.
        """

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
            return min(conc_list), sum(conc_list) / len(conc_list), max(
                conc_list)

    def display_cross_table(self, stat: Stats):
        """"Print a table according to the input given."""

        filtered_zips = [item for item in self._zips if self._zips[item]
                         is True]
        print(f"{' ':7}", end="")
        for item in self._times:
            print(f"{item:>8}", end="")
        print()
        for item in filtered_zips:
            print(f"{item:<7}", end="")
            for other_item in self._times:
                try:
                    value = self._cross_table_statistics(item,
                                                         other_item)[stat.value]
                except NoMatchingItems:
                    print(f"{'N/A':>8}", end="")
                else:
                    print(f"{value:>8.2f}", end="")
            print()


def print_menu():
    """Print the menu."""
    print("")
    print("Main Menu:")
    print("1 - Print Minimum Particulate Concentration by Zip Code and Time")
    print("2 - Print Average Particulate Concentration by Zip Code and Time")
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
        elif user_input == 1 or user_input == 2 or user_input == 3:
            enum_list = []
            for item in Stats:
                enum_list.append(item)
            if len(my_dataset._zips) == 0 or len(my_dataset._times) == 0:
                print("Please load your dataset first")
            else:
                my_dataset.display_cross_table(enum_list[user_input - 1])

        elif user_input == 4:
            print("This function isn't available yet. Pick another option!")
        elif user_input == 5:
            my_dataset.load_default_data()

        else:
            print("This option isn't listed in the menu! Try again.")
            print("")


def main():
    """Ask for user's name and valid header and execute menu code."""

    unit_test()
    """
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
    """


if __name__ == "__main__":
    main()


"""
        Evening Morning  Midday
12345       N/A    1.10     N/A
94022      3.20    2.20    1.00
94040       N/A    1.00     N/A
        Evening Morning  Midday
12345       N/A    1.10     N/A
94040       N/A    1.00     N/A
        Evening Morning  Midday

Process finished with exit code 0
"""
