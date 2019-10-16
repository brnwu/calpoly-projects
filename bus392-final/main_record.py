#     _____ _   _ _____   _____  _____  _____
#    | ___ \ | | /  ___| |____ ||  _  |/ __  \
#    | |_/ / | | \ `--.      / /| |_| |`' / /'
#    | ___ \ | | |`--. \     \ \\____ |  / /
#    | |_/ / |_| /\__/ / .___/ /.___/ /./ /___
#    \____/ \___/\____/  \____/ \____/ \_____/
#
#  F   I   N   A   L   P   R   O   J   E   C   T
#
#          By Brian Wu & James Graham
#           With Professor Neal King
#


import csv
import pickle


def main():
    print("******************************************************************")
    print("                  Welcome to CSV Record Analysis                  ")
    print("******************************************************************")
    csv_dict = csv_reader()
    max_profit(csv_dict)
    min_profit(csv_dict)
    top_10(csv_dict, "highest")
    top_10(csv_dict, "lowest")
    order_search(csv_dict)
    pickler(csv_dict)


def csv_reader():
    csv_dict = {}
    # Creates sentinel if FileNotFoundError exception caught to prompt for another filename input
    indicator = False
    # Prompts user again for file input if exception caught
    while indicator is False:
        infile = input("Please input name of CSV file: ")
        # infile = "records.csv"
        try:
            with open(infile, newline='') as csv_file:
                csv_report = csv.reader(csv_file, delimiter=',')
                # Sets a counter that sets the header to key -1 to be removed later
                for row in csv_report:
                    # Instantiates a 'Record' object with data in row with key as index value
                    # Dictionary can now be searched by index (row # of csv = dictionary key)
                    csv_dict[(row[6])] = Record(row)
                # Removes header key & definition from dictionary
                del csv_dict["Order ID"]
                # Sets sentinel to True to stop while loop
                indicator = True
                # Returns the dictionary object to main() to run analysis functions
                return csv_dict
        except FileNotFoundError:
            print("Error: CSV file could not be found. Enter a valid CSV file in the same directory.\n")
        # Broad except clause that catches if the file cannot be parsed by csv module
        # (PEP says not to make broad except clauses but...)
        # Possible errors include UnicodeDecodeError (can't convert encoding format), IndexError (wrong length), etc.
        # except:
            # print("Error: Unreadable file type. Please enter a valid CSV file.\n")


def max_profit(csv_dict):
    print("\nORDER STATISTICS")
    print("******************************************************************")
    profit_list = []
    # Appends list of total profit from Record objects in dictionary to temporary list
    # "key, values" unpacks the tuple output from .items() method
    for key, values in csv_dict.items():
        profit_list.append((float(values.__get_total_profit__()), values.__get_order_id__()))
    # Sets key of the highest profit from index in the list
    order_id = profit_list[profit_list.index(max(profit_list[0]))][1]
    # Matches key of highest profit to Record objects in dictionary, gets values using get methods, and prints
    # a formatted output of the values from the object
    print('{:<20}'.format("The max profit is:"),
          '{:<20}'.format(dollar_format(csv_dict[order_id].__get_total_profit__())))
    print('{:<20}'.format("Found in order #:"), '{:<20}'.format(csv_dict[order_id].__get_order_id__()))
    print('{:<20}'.format("At index value:"), '{:<20}'.format(order_id), "\n")
    # Deletes temporary list to free up memory
    del profit_list


def min_profit(csv_dict):
    profit_list = []
    # Appends list of total profit from Record objects in dictionary to temporary list
    # "key, values" unpacks the tuple output from .items() method
    for key, values in csv_dict.items():
        profit_list.append(float(values.__get_total_profit__()))
    # Sets key of the highest profit from index in the list
    location = profit_list.index(min(profit_list))
    # Matches key of highest profit to Record objects in dictionary, gets values using get methods, and prints
    # a formatted output of the values from the object
    print('{:<20}'.format("The min profit is:"),
          '{:<20}'.format(dollar_format(csv_dict[location].__get_total_profit__())))
    print('{:<20}'.format("Found in order #:"), '{:<20}'.format(csv_dict[location].__get_order_id__()))
    print('{:<20}'.format("At index value:"), '{:<20}'.format(location), "\n")
    # Deletes temporary list to free up memory
    del profit_list


def top_10(csv_dict, parameter):
    profit_list = []
    top_10_list = []
    # Appends list of total profit from Record objects in dictionary to temporary list
    # "key, values" unpacks the tuple output from .items() method
    for key, values in csv_dict.items():
        profit_list.append(float(values.__get_total_profit__()))
    # Used to combine the top 10 functions into one, calculates highest if top_10() called with "highest"
    if parameter == "highest":
        # Sets a count to calculate only top 10 values
        count = 0
        while count < 10:
            # Sets a temporary variable to the max value in profit list
            max_value = max(profit_list)
            # Finds the "location" = index = key of the max value
            location = profit_list.index(max_value)
            # Uses Record methods to pull order ID, order date, and total profit from Record object at key
            top_10_list.append((csv_dict[location].__get_order_id__(), csv_dict[location].__get_order_date__(),
                                csv_dict[location].__get_total_profit__()))
            # Sets max profit to 0 so that while loop can find next highest value on next loop
            profit_list[location] = 0
            count += 1
        # Sends data to output function to format and print the top 10 values
        top_10_output(top_10_list, parameter)
        # Clears memory of temporary lists
        del profit_list
        del top_10_list
    elif parameter == "lowest":
        count = 0
        while count < 10:
            # Sets a temporary variable to the max value in profit list
            max_value = min(profit_list)
            # Finds the "location" = index = key of the max value
            location = profit_list.index(max_value)
            # Uses Record methods to pull order ID, order date, and total profit from Record object at key
            top_10_list.append((csv_dict[location].__get_order_id__(), csv_dict[location].__get_order_date__(),
                                csv_dict[location].__get_total_profit__()))
            # Sets min profit to max profit so that while loop can find next lowest value on next loop
            profit_list[location] = max(profit_list)
            count += 1
        # Sends data to output function to format and print the top 10 values
        top_10_output(top_10_list, parameter)
        # Clears memory of temporary lists
        del profit_list
        del top_10_list


def order_search(csv_dict):
    print("Order Search Function")
    print("******************************************************************")
    search = int(input("Please enter an order ID to locate: "))
    if is_valid(search) is True:
        id_list = []
        # Appends all order IDs in dictionary to a temporary list
        for key, values in csv_dict.items():
            id_list.append(int(values.__get_order_id__()))
        # Tries to search for the value in the list using index()
        try:
            # Index in id_list corresponds to dictionary key value of location
            location = id_list.index(search)
            # Pulls data from dictionary definition at location, prints formatted output
            print('{:<20}'.format("Order ID:"), '{:<20}'.format(csv_dict[location].__get_order_id__()))
            print('{:<20}'.format("Ship Date:"), '{:<20}'.format(csv_dict[location].__get_ship_date__()))
            print('{:<20}'.format("Total Revenue:"),
                  '{:<20}'.format(dollar_format(csv_dict[location].__get_total_revenue__())))
        # If it can't find the Order ID, catches the exception
        except ValueError:
            print("Error: Order ID not found. Enter another Order ID.\n")
            # Recursively calls order_search() with csv_dict object if ID is not found
            order_search(csv_dict)
        # Delete id_list from memory
        del id_list
    else:
        print("Error: Invalid Order ID (must be an integer and 9 digits long). Please try again.")
        order_search(csv_dict)


def pickler(csv_dict):
    print("\nDeserialized Object")
    print("******************************************************************")
    # Creates file called "record_objects.dat" with write/binary specified for file handling
    with open("record_objects.dat", "wb") as f:
        count = 0
        # Pickles first 100 objects (this while loop can be set to the entire CSV in the future!)
        while count < 100:
            # Pickles each line IN ORDER into record_objects.dat
            pickle.dump(csv_dict[count], f)
            count += 1
    print("This is record #10 out of 100:")
    with open("record_objects.dat", "rb") as f:
        output_list = []
        # Unpickles the first 10 objects (this can be set to the entire CSV in the future as well!)
        for i in range(0, 10):
            output_list.append(pickle.load(f))
        # Calls Record object methods to print and format order ID, ship date, and profit output
        print('{:<20}'.format("Order ID:"), '{:<20}'.format(output_list[9].__get_order_id__()))
        print('{:<20}'.format("Ship Date:"), '{:<20}'.format(output_list[9].__get_ship_date__()))
        print('{:<20}'.format("Total Profit:"), '{:<20}'.format(dollar_format(output_list[9].__get_total_profit__())))


########################################################################################################################


# This function is solely to format the top 10 list output
def top_10_output(top_10_list, parameter):
    # Prints header based on parameter specified when called
    if parameter == "highest":
        print("Top 10 highest total profit items\n")
    elif parameter == "lowest":
        print("Top 10 lowest total profit items\n")
    # Uses string formatting to left align with 15 spaces to create three columns
    print("\t", '{:<15}'.format("Order ID"), '{:<15}'.format("Order Date"), '{:<15}'.format("Total Profit"))
    # Uses string formatting with same align / spacing to fill in rows
    for row in top_10_list:
        print("\t", '{:<15}'.format(row[0]), '{:<15}'.format(row[1]), '{:<15}'.format(dollar_format(row[2])))
    print("\n")


def is_valid(entry):
    return entry is int and len(str(entry)) == 9


def dollar_format(dollar):
    # Formats the input (string > float > string) with commas and dollar symbol
    return "$ {:,.2f}".format(float(dollar))


########################################################################################################################


class Record:
    def __init__(self, row):
        # This class stores all of the columns in the csv file as attributes
        # Though, this can break easily if the columns are out of order, missing, etc.
        self.region = row[0]
        self.country = row[1]
        self.item_type = row[2]
        self.sales_channel = row[3]
        self.order_priority = row[4]
        self.order_date = row[5]
        self.order_id = row[6]
        self.ship_date = row[7]
        self.units_sold = row[8]
        self.unit_price = row[9]
        self.unit_cost = row[10]
        self.total_revenue = row[11]
        self.total_cost = row[12]
        self.total_profit = row[13]

    def __str__(self):
        return self.order_id, self.order_date, self.total_profit

    # The record file is read only for security, so no set methods!
    # def __set_order_date__(self, order_date):
    #     self.order_date = order_date
    #
    # def __set_order_id__(self, order_id):
    #     self.order_id = order_id
    #
    # def __set_total_profit__(self, total_profit):
    #     self.total_profit = total_profit
    #
    # def __set_total_revenue__(self, total_revenue):
    #     self.total_revenue = total_revenue
    #
    # def __set_ship_date__(self, ship_date):
    #     self.ship_date = ship_date

    # Only defined 5 get methods because these 5 attributes were a part of the project specifications

    def __get_order_date__(self):
        return self.order_date

    def __get_order_id__(self):
        return self.order_id

    def __get_total_profit__(self):
        return self.total_profit

    def __get_total_revenue__(self):
        return self.total_revenue

    def __get_ship_date__(self):
        return self.ship_date


if __name__ == "__main__":
    main()


# Thanks for a great quarter!
# - Brian & James

