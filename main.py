import pip
import robin_stocks as rs
import pandas as pd
# from tkinter import *
import tkinter as tk


# change store session if you want to remember password
#rs.login(username='', password='', expiresIn=86400, by_sms=True, store_session=True)
#rs.logout()



def click_transactions():
    # Get Deposits and Withdrawals in Robinhood
    transact = rs.get_bank_transfers()
    card = rs.get_card_transactions()

    dep = sum(
        float(x['amount']) for x in transact if
        (x['direction'] == 'deposit') and (x['state'] == 'completed'))
    withd = sum(
        float(x['amount']) for x in transact if
        (x['direction'] == 'withdraw') and (x['state'] == 'completed'))
    debit = sum(float(x['amount']['amount']) for x in card if
                (x['direction'] == 'debit' and (x['transaction_type'] == 'settled')))
    reversal_fees = sum(
        float(x['fees']) for x in transact if (x['direction'] == 'deposit') and (x['state'] == 'reversed'))

    converted_deposits = str(round(dep, 2))
    converted_withdrawals = str(round(withd, 2))
    converted_total = str(round(dep - withd - debit - reversal_fees, 2))
    transaction_text = "All in all you have deposited: " + converted_deposits + " USD " + "and Withdrawn: " + converted_withdrawals + " USD " + '\n' + \
                       "The total amount you have put into Robinhood is " + converted_total + " USD"
    print(transaction_text)

    # print transcactions in text box
    label = tk.Label(root)
    label.pack()
    tab_title = tk.Tk()
    tab_title.title("Transactions")
    converted_deposits = str(round(dep, 2))
    converted_withdrawals = str(round(withd, 2))
    converted_total = str(round(dep - withd - debit - reversal_fees, 2))
    transaction_text = "All in all you have deposited: " + converted_deposits + " USD " + "and Withdrawn: " + converted_withdrawals + " USD " + '\n' + \
                       "The total amount you have put into Robinhood is " + converted_total + " USD"
    label = tk.Label(tab_title, text=transaction_text)
    label.pack()


def click_orders():
    # Get total number of buy/sell orders ever placed

    # For stocks
    all_orders = rs.orders.get_all_stock_orders()
    stock_count = 0
    for x in all_orders:
        stock_count += 1

    # For crypto
    all_orders2 = rs.orders.get_all_crypto_orders()
    crypto_count = 0
    for x in all_orders2:
        crypto_count += 1

    # For options
    option_order = rs.orders.get_all_option_orders()
    option_count = 0
    for x in option_order:
        option_count += 1

    print("The total number of buy/sell orders you have placed is:", stock_count + crypto_count + option_count)

    # print total orders in text box
    label = tk.Label(root)
    label.pack()
    tab_title = tk.Tk()
    tab_title.title("Transactions")
    converted_total = str(stock_count + crypto_count + option_count)
    transaction_text = "The total number of buy/sell orders you have placed is: " + converted_total
    label = tk.Label(tab_title, text=transaction_text)
    label.pack()

def click_login():
    # GUI to enter username and password
    #root = tk.Tk()
    window = tk.Toplevel(root)
    # setting the windows size
    window.geometry("600x400")

    # declaring string variable
    # for storing name and password
    name_var = tk.StringVar()
    passw_var = tk.StringVar()
    # defining a function that will
    # get the name and password and
    # print them on the screen
    def submit():
        name = name_entry.get()
        password = passw_var.get()

        print("The name is : " + name)
        print("The password is : " + password)
        rs.login(username=name, password=password, expiresIn=86400, by_sms=True,
                 store_session=True)
        name_var.set("")
        passw_var.set("")

    # creating a label for
    # name using widget Label
    name_label = tk.Label(window, text='Username',
                          font=('calibre',
                                10, 'bold'))

    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(window,
                          textvariable=name_var, font=('calibre', 10, 'normal'))

    # creating a label for password
    passw_label = tk.Label(window,
                           text='Password',
                           font=('calibre', 10, 'bold'))

    # creating a entry for password
    passw_entry = tk.Entry(window,
                           textvariable=passw_var,
                           font=('calibre', 10, 'normal'),
                           show='*')

    # creating a button using the widget
    # Button that will call the submit function
    sub_btn = tk.Button(window, text='Submit',
                        command=submit)

    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)

    # performing an infinite loop
    # for the window to display
    #root.mainloop()

def click_logout():
    rs.logout()


# makes button for the two
root = tk.Tk()
root.title("Main Menu")
btn0 = tk.Button(root, text="Login", command=click_login)
btn1 = tk.Button(root, text="Get Your Transactions", command=click_transactions)
btn2 = tk.Button(root, text="Get the number of orders you have ever placed", command=click_orders)
#btn4 = tk.Button(root, text="Logout", command=click_logout())
btn0.pack()
btn1.pack()
btn2.pack()
#btn4.pack()
root.mainloop()
