import robin_stocks as rs
import tkinter as tk


# Debug; ignore these two lines
# rs.login(username='', password='', expiresIn=86400, by_sms=True, store_session=True)
# rs.logout()

# This function creates a log in box where you can enter your credentials to use the actual program
def click_login():
    window = tk.Toplevel(root)

    window.geometry("500x350")

    name_var = tk.StringVar()
    passw_var = tk.StringVar()

    def submit():
        name = name_display.get()
        password = passw_var.get()

        print("username is: " + name)
        print("password is: " + password)
        rs.login(username=name, password=password, expiresIn=86400, by_sms=True, store_session=True)
        name_var.set("")
        passw_var.set("")

    name_gui = tk.Label(window, text='Username', font=('calibre', 10, 'bold'))

    name_display = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'))

    passw_gui = tk.Label(window, text='Password', font=('calibre', 10, 'bold'))

    passw_display = tk.Entry(window, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

    submit_button = tk.Button(window, text='Submit', command=submit)

    # Displays the actual parts on the GUI
    name_gui.grid(row=0, column=0)
    name_display.grid(row=0, column=1)
    passw_gui.grid(row=1, column=0)
    passw_display.grid(row=1, column=1)
    submit_button.grid(row=2, column=1)


# This function gets the number of deposits and withdrawals you have ever done
def click_transactions():
    transact = rs.get_bank_transfers()
    card = rs.get_card_transactions()

    # Get the deposits, withdrawals, debits, and reversal fees for your account
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

    # Must convert to strings to be used properly in the text box
    converted_deposits = str(round(dep, 2))
    converted_withdrawals = str(round(withd, 2))
    converted_total = str(round(dep - withd - debit - reversal_fees, 2))
    transaction_text = "All in all you have deposited: " + converted_deposits + " USD " + "and Withdrawn: " \
                       + converted_withdrawals + " USD " + '\n' + \
                       "The total amount you have put into Robinhood is " + converted_total + " USD"
    print(transaction_text)

    # Print transactions in the actual text box
    label = tk.Label(root)
    label.pack()
    tab_title = tk.Tk()
    tab_title.title("Transactions")
    converted_deposits = str(round(dep, 2))
    converted_withdrawals = str(round(withd, 2))
    converted_total = str(round(dep - withd - debit - reversal_fees, 2))
    transaction_text = "All in all you have deposited: " + converted_deposits + " USD " + "and Withdrawn: " \
                       + converted_withdrawals + " USD " + '\n' + \
                       "The total amount you have put into Robinhood is " + converted_total + " USD"
    label = tk.Label(tab_title, text=transaction_text)
    label.pack()


# This number gets the total number of buy/sell orders ever placed
def click_orders():
    # Gets the buy/sell orders for stocks
    all_orders = rs.orders.get_all_stock_orders()
    stock_count = 0
    for _ in all_orders:
        stock_count += 1

    # Gets the buy/sell orders for crypto
    all_orders2 = rs.orders.get_all_crypto_orders()
    crypto_count = 0
    for _ in all_orders2:
        crypto_count += 1

    # Gets the buy/sell orders for options
    option_order = rs.orders.get_all_option_orders()
    option_count = 0
    for _ in option_order:
        option_count += 1

    print("The total number of buy/sell orders you have placed is:", stock_count + crypto_count + option_count)

    # Print the total number of orders in the actual text box
    label = tk.Label(root)
    label.pack()
    tab_title = tk.Tk()
    tab_title.title("Transactions")
    converted_total = str(stock_count + crypto_count + option_count)
    transaction_text = "The total number of buy/sell orders you have placed is: " + converted_total
    label = tk.Label(tab_title, text=transaction_text)
    label.pack()


# This function logs you out
def click_logout():
    rs.logout()


# These actually make the buttons and runs X program when the button is clicked
root = tk.Tk()
root.title("Main Menu")
btn0 = tk.Button(root, text="Login", command=click_login)
btn1 = tk.Button(root, text="Get Your Transactions", command=click_transactions)
btn2 = tk.Button(root, text="Get the number of orders you have ever placed", command=click_orders)
# btn4 = tk.Button(root, text="Logout", command=click_logout())
btn0.pack()
btn1.pack()
btn2.pack()
# btn4.pack()
root.mainloop()
