import os
import yfinance as yf
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    try:
        ticker = yf.Ticker(request.form['ticker'])
        data = ticker.history().tail(1)['Close'].iloc[0]
    except:
        return render_template('index.html', data="Error: Invalid ticker symbol")

    return render_template('index.html', data='{:.2f}'.format(data))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)