import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

api_key = 'fc62c57578864e4da8863911995bc617' # reemplaza TU_API_KEY con tu propia API Key

historical_data = {}

def con(base_currency, target_currency):
    base = base_currency # establece la moneda base en dólares estadounidenses
    target = target_currency 

def dias():
    for i in range(7):
        date = datetime.date.today() - datetime.timedelta(days=i)
        url = f"https://openexchangerates.org/api/historical/{date}.json?app_id={api_key}&base={base_currency}&symbols={target_currency}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][target_currency]
        historical_data[str(date)] = rate

 # establece la moneda objetivo en pesos mexicanos
         # crea un diccionario para almacenar los datos históricos
con("USD", "CLP")

fecha = list(historical_data.keys())
fluctuacion = list(historical_data.values())

plt.plot(fecha, fluctuacion)
plt.show()
