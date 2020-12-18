import robin_stocks as rs
import tkinter as tk

# This API was used: https://github.com/jmfernandes/robin_stocks

# Debug; ignore these two lines
#rs.login(username='', password='', expiresIn=86400, by_sms=True, store_session=True)


#rs.logout()

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


def limit_order_crypto():
    window2 = tk.Toplevel(root)

    window2.geometry("500x350")

    symbol_var = tk.StringVar()
    quantity_var = tk.StringVar()
    price_var = tk.StringVar()

    def submit2():
        quantity = quantity_var.get()
        price = price_var.get()
        symbol = symbol_var.get()
        price_v2 = float(price)
        quantity_v2 = float(quantity)
        print("symbol: " + symbol)
        print("quantity: " + quantity)
        print("Limit Price (max price you are willing to pay): " + price)
        rs.orders.order_buy_crypto_limit(symbol, quantity_v2, price_v2, timeInForce='gtc')
        symbol_var.set("")
        quantity_var.set("")
        price_var.set("")

    symbol_gui = tk.Label(window2, text='Symbol', font=('calibre', 10, 'bold'))

    symbol_display = tk.Entry(window2, textvariable=symbol_var, font=('calibre', 10, 'normal'))

    quant_gui = tk.Label(window2, text='Quantity', font=('calibre', 10, 'bold'))

    quant_display = tk.Entry(window2, textvariable=quantity_var, font=('calibre', 10, 'normal'))

    price_gui = tk.Label(window2, text='Price', font=('calibre', 10, 'bold'))

    price_display = tk.Entry(window2, textvariable=price_var, font=('calibre', 10, 'normal'))

    submit_button = tk.Button(window2, text='Submit', command=submit2)

    # Displays the actual parts on the GUI
    symbol_gui.grid(row=0, column=0)
    symbol_display.grid(row=0, column=1)
    quant_gui.grid(row=1, column=0)
    quant_display.grid(row=1, column=1)
    price_gui.grid(row=2, column=0)
    price_display.grid(row=2, column=1)
    submit_button.grid(row=3, column=1)


def limit_order_stock():
    window3 = tk.Toplevel(root)

    window3.geometry("500x350")

    symbol_var = tk.StringVar()
    quantity_var = tk.StringVar()
    price_var = tk.StringVar()

    def submit3():
        quantity = quantity_var.get()
        price = price_var.get()
        symbol = symbol_var.get()
        price_v2 = float(price)
        quantity_v2 = float(quantity)
        print("symbol: " + symbol)
        print("quantity: " + quantity)
        print("Limit Price (max price you are willing to pay): " + price)
        rs.orders.order_buy_limit(symbol, quantity_v2, price_v2, timeInForce='gtc', extendedHours=False)
        symbol_var.set("")
        quantity_var.set("")
        price_var.set("")

    symbol_gui = tk.Label(window3, text='Symbol', font=('calibre', 10, 'bold'))

    symbol_display = tk.Entry(window3, textvariable=symbol_var, font=('calibre', 10, 'normal'))

    quant_gui = tk.Label(window3, text='Quantity', font=('calibre', 10, 'bold'))

    quant_display = tk.Entry(window3, textvariable=quantity_var, font=('calibre', 10, 'normal'))

    price_gui = tk.Label(window3, text='Price', font=('calibre', 10, 'bold'))

    price_display = tk.Entry(window3, textvariable=price_var, font=('calibre', 10, 'normal'))

    submit_button = tk.Button(window3, text='Submit', command=submit3)

    # Displays the actual parts on the GUI
    symbol_gui.grid(row=0, column=0)
    symbol_display.grid(row=0, column=1)
    quant_gui.grid(row=1, column=0)
    quant_display.grid(row=1, column=1)
    price_gui.grid(row=2, column=0)
    price_display.grid(row=2, column=1)
    submit_button.grid(row=3, column=1)


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
btn5 = tk.Button(root, text="Limit Order Buy (Crypto)", command=limit_order_crypto)
btn6 = tk.Button(root, text="Limit Order Buy (Stock)", command=limit_order_stock)
btn0.pack()
btn1.pack()
btn2.pack()
# btn4.pack()
btn5.pack()
btn6.pack()
root.mainloop()
