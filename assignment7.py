"""This program greets the user, asks them to select a header, and presents a
menu for them to choose from. After they choose, the program lets them know if
their choice was okay.
"""
from enum import Enum


def unit_test():
    """Testing enum class application to display concentration data
    in a user-friendly manner.
    """
    my_dataset = DataSet()
    my_dataset.load_default_data()
    print("The following Zip Codes are loaded:")
    for zip_code in my_dataset._zips:
        print(zip_code)
    print("")
    print("The following Times of Day are loaded:")
    for time_of_day in my_dataset._times:
        print(time_of_day)
    print("")
    my_zip = "94040"
    my_time = "Morning"
    data_tuple = my_dataset._cross_table_statistics(my_zip, my_time)
    """maybe i I didn't understand the assignment, but was I supposed to use 
    this tuple above?
    """
    for item in Stats:
        print(f"The {item.name} for {my_zip}, {my_time} is {item.value}")


class Stats(Enum):
    MIN = 1.0
    AVG = 2.0
    MAX = 3.0


class EmptyDatasetError(Exception):
    pass


class NoMatchingItems(Exception):
    pass


class DataSet:
    def __init__(self, header: str = ""):
        self._data = None
        self.header = header
        self._zips = []
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
        zip_codes = set()
        day_times = set()
        for tup in self._data:
            for value in tup:
                try:
                    int(value)
                except:
                    day_times.add(value)
                else:
                    if not type(value) == float:
                        zip_codes.add(value)
        self._zips = list(zip_codes)
        self._times = list(day_times)

    def load_default_data(self):
        """creating a list of tuples with sample data"""
        self._data = [("12345", "94022", "94040", "94022", "94040", "94022"),
                      ("Morning", "Morning", "Morning", "Midday", "Morning",
                       "Evening"), (1.1, 2.2, 3.0, 1.0, 1.0, 3.2)]
        self._initialize_labels()

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
The following Zip Codes are loaded:
94040
12345
94022

The following Times of Day are loaded:
Evening
Midday
Morning

The MIN for 94040, Morning is 1.0
The AVG for 94040, Morning is 2.0
The MAX for 94040, Morning is 3.0

Process finished with exit code 0
"""