from locale import currency
from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/currency/<currency>")
def api(currency):
    exchange_rate_key = os.environ.get('EXCHANGERATE_KEY')
    url = "https://v6.exchangerate-api.com/v6/" + exchange_rate_key + "/pair/USD/" + currency
    r = requests.get(url)
    return r.json()