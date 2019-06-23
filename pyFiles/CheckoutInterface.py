from pyFiles import Transcation as tN
from tkinter import *
from tkinter import messagebox
import re

_SYSTEM_NAME = "BIG-Mart CHECKOUT SYSTEM"
_SYSTEM_SIZE = "700x500"
_SYSTEM_PAYMENT_SIZE = "450x350"

SET_VARIABLE = StringVar


class CheckoutInterface:

    def __init__(self):
        """Checkout System"""
        self.scr = Tk()
        self.accept_amt = StringVar(self.scr)
        self.enter_bar_code = StringVar(self.scr)

    def window_(self):
        self.scr.title(_SYSTEM_NAME)
        self.scr.geometry(_SYSTEM_SIZE)
        self.scr.resizable(FALSE, FALSE)
        self.scr.config(bg="blue")
        return self.scr

    def clear_entry(self):
        self.enter_bar_code.set("")
        self.accept_amt.set("")

    def exit(self):
        if tran.amount_received == 0.0:
            messagebox.showinfo("Thanking", "Thank you for visiting at BIG-Mart")
        else:
            messagebox.showinfo("Thanking", "Thank you for shopping at BIG-Mart")
        self.scr.after(500,self.scr.destroy())

    def home(self, scr):
        global tran
        frame = Frame(scr, height=100, width=100)
        frame.pack(fill=X)
        label = Label(frame, text="Welcome to BIG-Mart", width=36, fg="blue", font=("Elephant", 20))
        label.grid()
        
        """frame 1"""
        frame1 = Frame(scr, width=700 / 2, height=440, bg="blue", bd=3)
        frame1.pack(anchor=W, fill=BOTH)
        enter_button = Button(frame1, text="Enter", width="10", height="3", bg="green", activebackground="green",
                              font=("courier", 10),
                              command=lambda: self.inject_bar_code())
        enter_button.grid(row=6, column=0)
        clear_button = Button(frame1, text="Clear", width="10", height="3", bg="red", activebackground="red",
                              font=("courier", 10), command=lambda: self.clear_entry())
        clear_button.grid(row=6, column=1)
        pay_button = Button(frame1, text="Pay", width="10", height="3", bg="light blue", activebackground="blue",
                            font=("courier", 10), command=lambda: self.payment_form())
        pay_button.grid(row=6, column=2)
        exit_button = Button(frame1, text="Exit", width="10", height="3", activebackground="red", font=("courier", 10),
                             command=lambda: self.exit())
        exit_button.grid(row=6, column=3)
        text_entry = Entry(frame1, textvariable=self.enter_bar_code, font=("arial", 10), bg="Black", fg="white")
        text_entry.grid(row=1, column=0, ipadx=111, ipady=5, columnspan=5, rowspan=5)
        text_entry.focus_set()
        label2 = Label(frame1, text="Enter Item Code", font=("Times Roman", 15), bg="blue", fg="white")
        label2.grid(row=0, column=0, columnspan=5, pady=5)
        label3 = Label(frame1, text="Enter Product/ \n Final Receipt", font=("Times Roman", 17), bg="blue", fg="white")
        label3.grid(row=0, column=6, rowspan=7, sticky=E, ipadx="70")
        enter_button.columnconfigure(0,weight=1)
        clear_button.columnconfigure(1,weight=1)
        pay_button.columnconfigure(2,weight=1)
        exit_button.columnconfigure(3,weight=1)

        """FRAME 2"""
        global frame2
        frame2 = Frame(scr, width=100, height=440, bg="Black")
        frame2.pack(anchor=W, side=TOP)
        scroll = Scrollbar(frame2)
        transaction_text_widget = Text(frame2, height=19, width=44, bg="Black", fg="white", font=("arial", 10))
        transaction_text_widget.grid(row=0, column=0)
        transaction_text_widget["yscrollcommand"] = scroll.set
        scroll.grid(row=0, column=1, sticky=NS)
        scroll.config(command=transaction_text_widget.yview)
        # insert the file value in Text for Display

        transaction_text_widget.config(state=NORMAL)
        transaction_text_widget.delete("1.0", END)
        transaction_text_widget.insert(END, tran.display_all_product())
        transaction_text_widget.config(state="disable")

        global text_eidget_amount
        scroll1 = Scrollbar(frame2)
        text_eidget_amount = Text(frame2, height=20, width=39, bg="sky blue", fg="black", font=("arial", 12))
        text_eidget_amount.grid(row=0, column=2)
        text_eidget_amount["yscrollcommand"] = scroll1.set
        scroll1.grid(row=0, column=3, sticky=NS)
        scroll1.config(command=text_eidget_amount.yview)
        text_eidget_amount.config(state=DISABLED)

    def inject_bar_code(self):
        # #     insert into Description Activity
        bar_code = self.enter_bar_code.get()
        if bar_code.isdigit() and bar_code is not None:
            tran.scan_item(bar_code)
            text_eidget_amount.config(state=NORMAL)
            text_eidget_amount.delete("1.0", END)
            text_eidget_amount.insert(END, tran.print_scan_products())
            text_eidget_amount.config(state="disable")
        else:
            messagebox.showerror("Error", "Please enter specified item code")

    """TOP LEVEL FORM"""

    """SECOND SCREEN """

    # 2ND SCREEN FROM HERE

    def payment_form(self):
        global payment_screen
        payment_screen = Toplevel()
        if tran.temp_amount <= 0.0:
            payment_screen.destroy()
            messagebox.showwarning("Warning", "Press the Enter button after entering code ")
        else:
            payment_screen.title("Checkout System/ Payment")
            payment_screen.geometry(_SYSTEM_PAYMENT_SIZE)
            payment_screen.resizable(FALSE, FALSE)
            payment_screen.config(bg="blue")
            self.transaction_form(payment_screen)

    def transaction_form(self, pay_screen):
        """Frame 1"""
        global entry_amt
        global button_amt
        payment_frame1 = Frame(pay_screen, width=100, height=100, bg="blue")
        payment_frame1.pack(pady=10)
        labe10_amt = Label(payment_frame1, text="Total Due $" + str(tran.total_amount_due), font=('arial', 20),
                           bg="blue",
                           fg="RED")
        labe10_amt.grid(row=0, column=0)
        label_amt = Label(payment_frame1, text=" Amount", font=('arial', 20), bg="blue", fg="white")
        label_amt.grid(row=0, column=1)
        entry_amt = Entry(payment_frame1, textvariable=self.accept_amt, width=7, font=('arial', 25), bg="white",
                          fg="black")
        entry_amt.grid(row=0, column=2, columnspan=4)

        button_amt = Button(payment_frame1, text="Pay", bg="green", width="8", height="3",
                            command=lambda: self.display_activity(self.accept_amt.get()))
        button_amt.grid(row=1, column=3)

        button_amt = Button(payment_frame1, text="Delete", bg="red", width="8", height="3",
                            command=lambda: self.clear_entry())
        button_amt.grid(row=1, column=4, sticky=W)

        payment_frame1.columnconfigure(0,weight=1)
        entry_amt.columnconfigure(2,weight=1)
        button_amt.columnconfigure(3,weight=1)
        labe10_amt.columnconfigure(0,weight=1)
        label_amt.columnconfigure(1,weight=1)

        """Frame 2"""
        global payment_frame_for_transaction
        payment_frame_for_transaction = Frame(pay_screen, width=400, height=240, bg="black", bd=3)
        payment_frame_for_transaction.pack(fill=BOTH)

    def display_activity(self, entry_amount):
# =============================================================================
#         checks the numeric value and zero value like 00001
# =============================================================================
        number_format = re.compile("[0-9]+(\.[0-9]{1,9})?$") 
        zero_format = re.compile("^[1-9]|^[0-9]\.\d*$")
        if not (re.match(number_format, entry_amount) and re.match(zero_format,entry_amount)):
            entry_amt = -1
        else:
            entry_amt = float(entry_amount)

        if entry_amt > 0 and tran.amount_received <= tran.total_amount_due:
            tran.temp_amount -= entry_amt
            tran.amount_received += entry_amt
        label_display = Label(payment_frame_for_transaction, height=10, width=40, bg="black", fg="white",
                              text="Enter amount: " + str(entry_amt) + "\nReceived amount: " + str(
                                  tran.amount_received) + "\nTotal due: " +
                                   (("\nCurrent $: " + str(tran.temp_amount) if entry_amt >= 0 or entry_amt >=0.0
                                     else "\nwe don't accept -ve amount or\n non-numeric amount\n NOTICE: Enter natural number or decimal") if tran.temp_amount > 0.0 else "\n$0.0"),
                              font=("ariel", 15))
        label_display.grid(row=0, column=0)
        if tran.amount_received >= tran.total_amount_due:
            self.export(tran.amount_received)

    def export(self, amt):
        tran.export_to_file(amt)
        text_eidget_amount.config(state=NORMAL)
        text_eidget_amount.delete("1.0", END)
        text_eidget_amount.insert(END, tran.file_for_print_bill() + "\n")
        text_eidget_amount.config(state=DISABLED)
        if tran.temp_amount <= 0.0:
            tran.clearance_attributes()
            self.enter_bar_code.set("")
            self.accept_amt.set(0)
            payment_screen.after(500, payment_screen.destroy())       	
            messagebox.showinfo("Notice", "Payment Completed!")

    def make(self):
        self.scr.mainloop()


tran = tN.AmountTransaction()
