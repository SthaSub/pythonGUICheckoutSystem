"""
Product for readfile data
"""
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# path = "C:\\Users\\Newaz\PycharmProjects\CheckoutSystem"
FILE_NAME = "ProductStore.txt"
FORMATTER = "CODE  \tNAME  \t\tPRICE($)\n"


class ProductFile:
    ids = list()
    items = list()
    prices = []
    all_items = set()

    def __init__(self):
        scan_items = list()
        file = open(FILE_NAME, "r")
        lines = file.readlines()
        for line in lines:
            if line.startswith("p"):
                continue
            scan_items.append(line.split(":")[0].split())
        for iterate in scan_items:
            self.ids.append(iterate[0])  # index for id
            self.items.append(iterate[1])  # index for item
            self.prices.append(iterate[2])  # index for price
            self.all_items.add(iterate[0] + "\t" + iterate[1] + "\t\t" + iterate[2] + "\n")


    def setter_product(self):
        """"""

    def ids_(self):
        return self.ids

    def items_(self):
        return self.items

    def prices_(self):
        return self.prices

    def display_all_product(self):
        transaction_info = ""
        for al in self.all_items:
            transaction_info += al
        return FORMATTER + transaction_info
