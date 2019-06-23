#!/usr/bin/python
from pyFiles import ProductFile as pF
import os
from tkinter import messagebox

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))  # brings the absolute path from current location
transaction_file = os.path.join(THIS_FOLDER, "transaction_history.txt")
present_file = os.path.join(THIS_FOLDER, "current_transaction.txt")


class AmountTransaction(pF.ProductFile):
    product = list()

    # money = list()

    def __init__(self):
        super().__init__()
        self.total_amount_due = 0.0  # = float(total_amount_due) if total_amount_due else 0.0  # total due amount
        self.scan_items_name = list()  # scan_items_name or []  # scanned item list name
        self.scan_items_price = list()  # scan_items_price or []  # scanned item list price
        self.amount_received = 0.0  # float(amount_received) if amount_received else 0.0  # customer paid amount
        self.temp_amount = 0.0  # float(temp_amount) if temp_amount else 0.0  # define holding for temporary value of total amount
        self.code_current = 0.0
        self.product_lists = list()
        self.inner_product_list = list()
        self.final_list = set()

    def scan_item(self, some_product_bar_code):
        i = 0  # index of array
        isThereAnyItem = "No"  # checking if any item present
        for checkId in self.ids_():
            if some_product_bar_code == checkId:
                some_product = some_product_bar_code
                self.total_amount_due += float(self.prices_()[i])  # calculates the total scanned item price
                self.scan_items_price.append(self.prices_()[i])  # add item price in scanned item
                self.scan_items_name.append(self.items_()[i])  # adds item name in scanned item
                isThereAnyItem = "Yes"
                self.product.append(self.items_()[i] + " - \t\t" + " $ " + self.prices_()[i] + "\n")
                self.product_lists.append((some_product, self.prices_()[i], self.items_()[i]))
                self.inner_product_list.append((some_product, self.prices_()[i]))
            i = i + 1
        if isThereAnyItem == "No":
            self.product.append("This product does not exist in our inventory.\n")

        self.temp_amount = self.total_amount_due

    def print_final(self):
        add = 0.0
        count = 0

        for code, produce, item in self.product_lists:
            for bar, price in self.inner_product_list:
                if code == bar:
                    add += float(price)
                    count = count + 1
            self.final_list.add((item, str(count) + "\t$" + str(add), code))
            add = 0.0
            count = 0

    #    def print_product(self):
    #        for item,product,bar in self.final_list:
    #
    #            print(item,"",product)

    def print_scan_products(self):
        product_list = ""
        for num in self.product:
            product_list += num
        return product_list

    def clearance_attributes(self):
        self.total_amount_due = 0.0  # = float(total_amount_due) if total_amount_due else 0.0  # total due amount
        self.scan_items_name.clear()  # scan_items_name or []  # scanned item list name
        self.scan_items_price.clear()  # scan_items_price or []  # scanned item list price
        self.amount_received = 0.0  # float(amount_received) if amount_received else 0.0  # customer paid amount
        self.temp_amount = 0.0  # float(temp_amount) if temp_amount else 0.0  # define holding for temporary value of total amount
        self.product.clear()
        self.final_list.clear()
        self.product_lists.clear()
        self.inner_product_list.clear()

    def export_to_file(self, amt):
        red = self.read_file_for_export()
        record_count = self.bill_counter()
        """FOR RECORD IN FILE HISTORY"""

        f = open(transaction_file, "w+")
        new_detail = record_count + ") -----Final Receipt -----" + "\n" + "item        quantity    x   price" + "\n"
        new_detail += (self.scan_item_contain())
        new_detail += ("Total amount due:  	$" + str(self.total_amount_due) + "\n")
        new_detail += ("Amount received:   $" + str(amt) + "\n")
        new_detail += ("Change given: $ " + str(
            amt - self.total_amount_due) + "\n\n") if amt > self.total_amount_due else "\n"
        new_info = new_detail
        new_detail += red
        f.write(new_detail + "\n")
        f.close()

        """FOR PRINT CURRENT BILL"""
        current_file = open(present_file, "w+")
        current_file.write(new_info + "\n")
        current_file.close()

    @staticmethod
    def read_file_for_export():
        file = open(transaction_file, "r")
        line = file.readlines()
        file.close()
        add = ""
        for lee in line:
            add += lee
        line.clear()
        file.close()
        return add

    @staticmethod
    def bill_counter():
        lee = ""
        try:
            fil = open(transaction_file, "r")
            lins = fil.readline()
            fil.close()
            lee = lins[:2] if os.stat(transaction_file).st_size != 0 else "0"
            if lee.isdigit():
                "Yes Numeric two character"
            else:
                lee = ""
                lee = lins[:1] if os.stat(transaction_file).st_size != 0 else "0"
        except FileNotFoundError:
            messagebox.showerror("Error", "transaction_history.txt File NOT Found")
        coun = int(lee)
        coun = coun + 1
        return str(coun)

    def scan_item_contain(self):
        #        lit = self.product
        #        value = ""
        #        for lie in lit:
        #            if lie[:1] == "T":  # Skips the line if it detect the Statement like "This"
        #                continue
        #            value += lie
        #        return value
        self.print_final()
        lit = self.final_list
        value = ""
        for item, product, bar in lit:
            value += (item + " - \t" + product + "\n")
        return value

    @staticmethod
    def file_for_print_bill():
        bill = ""
        global bill_lines
        try:
            file_bill = open(present_file, "r")
            bill_lines = file_bill.readlines()
            file_bill.close()
        except FileNotFoundError:
            messagebox.showerror("Error", "current_transaction.txt File NOT Found")
        for file in bill_lines:
            bill += file + "\n"
        return bill
