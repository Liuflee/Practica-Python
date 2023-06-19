import tkinter as tk
from tkinter import messagebox
import urllib.request
import requests
import json
import time
import decimal
from PIL import Image, ImageTk

'''Dictionary with currency values'''
currencies = {
    "USD": 1.0,
    "EUR": 0.8329,
    "CLP": 772.9476,
    "JPY": 109.4494,
    "ARS": 217.439,
    "MXN": 18.092843
}

'''URL with cat images'''
url = "https://i.imgur.com/iNqMjGS.png"
cat, headers = urllib.request.urlretrieve(url)
url2 = "https://i.imgur.com/xZJ38rX.png"
cat2, headers2 = urllib.request.urlretrieve(url2)

def update_currency(api_key):
    """Updates exchange rates with the openexchangerates.org API"""
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = json.loads(response.text)["rates"]
        currencies.update(rates)
    else:
        raise Exception("Error obtaining exchange rates")
    
def convert_currency(currency_from, currency_to):
    """Converts an amount from one currency to another"""
    try:
        value_from = decimal.Decimal(currency_entry.get())
        conversion_rate = decimal.Decimal(currencies[currency_to]) / decimal.Decimal(currencies[currency_from])
        value_to = round((value_from * conversion_rate), 2)
        result_label.config(text=f"{value_to:,.2f} {currency_to}")
    except ValueError:
         messagebox.showerror("Error", "The entered amount is not a valid number")


def print_text(text, widget, speed):
    '''Function that prints the text progressively'''
    for i in range(len(text)):
        widget.config(text=text[:i+1])
        widget.update()
        time.sleep(speed)

def change_image():
    '''Changes the image'''
    global background_image
    new_image = Image.open(cat2)
    background_image = ImageTk.PhotoImage(new_image)
    canvas.create_image(0, 140, anchor='nw', image=background_image)


def change_function(*args):
    """Changes the button function to include currency conversion
    and image update"""
    currency_from = currency_option_from.get()
    currency_to = currency_option_to.get()
    button.config(command=lambda: (convert_currency(currency_from, currency_to), change_image()))

'''Creating the main window with its title'''
window = tk.Tk()
window.geometry("250x250")
window.title("Epic Converter 3: Now It's Personal")

update_currency("fc62c57578864e4da8863911995bc617")

'''Cat image'''
canvas = tk.Canvas(window, width=250, height=250)
canvas.pack()

background_image = Image.open(cat)
background_image = ImageTk.PhotoImage(background_image, format="PNG")
canvas.create_image(0, 160, anchor='nw', image=background_image)

'''Dropdown menu with the source currency'''
currency_options_from = ["USD", "EUR", "CLP", "JPY", "ARS", "MXN"]
currency_option_from = tk.StringVar(window)
currency_option_from.set(currency_options_from[0])

frame_from = tk.Frame(window)
frame_from.place(x=170, y=80)

menu_from = tk.OptionMenu(frame_from, currency_option_from, *currency_options_from)
menu_from.pack()

'''Dropdown menu with the destination currency'''
currency_options_to = ["USD", "EUR", "CLP", "JPY", "ARS", "MXN"]
currency_option_to = tk.StringVar(window)
currency_option_to.set(currency_options_to[0])

frame_to = tk.Frame(window)
frame_to.place(x=170, y=140)

menu_to = tk.OptionMenu(frame_to, currency_option_to, *currency_options_to)
menu_to.pack()

'''Label with a title inside the window'''
title = tk.Label()
title.pack()
title.place(x=50, y=10)
text_to_print = "Welcome to the epic converter\n by Anette"

'''Label that shows the result, it is updated later with the
convert_currency() function inside change_function()'''
result_label = tk.Label(window)
result_label.pack()
result_label.place(x=30, y=120)

'''Label located above the source currency menu'''
from_label = tk.Label(window)
from_label.pack()
from_label.place(x=170, y=60)
text_from = "From"

'''Label located above the destination currency menu'''
to_label = tk.Label(window)
to_label.pack()
to_label.place(x=170, y=120)
text_to = "To"

'''Label located above the number entry'''
amount_label = tk.Label(window)
amount_label.pack()
amount_label.place(x=30, y=80)
text_amount = "Amount to convert"

'''Number entry'''
currency_entry = tk.Entry(window)
currency_entry.pack()
currency_entry.place(x=30, y=100)

'''The print_text() function is called to write
all the text in the window progressively'''
print_text(text_to_print, title, 0.01)
print_text(text_amount, amount_label, 0.03)
print_text(text_from, from_label, 0.03)
print_text(text_to, to_label, 0.03)

'''Creating the button'''
button = tk.Button(window, text="Change")
button.pack()
button.place(x=100, y=200)

'''Changes the button function according to what is chosen in the dropdown menus'''
currency_option_from.trace("w", change_function)
currency_option_to.trace("w", change_function)

'''Main loop of the window, allows it to run'''
window.mainloop()