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


class Record:
    def __init__(self, row, count):
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
        self.index_value = count

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
