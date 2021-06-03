from typing import Mapping
from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/customerPage')
def customerPage():
    return render_template('customerPage.html')


@app.route('/logistic')
def logistic():
    return render_template('logistic.html')
    
@app.route('/bill')
def bill():
    return render_template('bill.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')


@app.route('/Chat')
def ChatPlacing():
    return render_template('ChatPlacing.html')


@app.route('/advertisement')
def advertisement():
    return render_template('advertisementplot.html')

@app.route('/records')
def records():
    return render_template('records.html')


@app.route('/stock_records')
def stock_records():
    return render_template('stock_records.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/Logisticmainpage')
def Logisticmainpage():
    return render_template('Logisticmainpage.html')

if __name__ == "__main__":
    app.run(debug=True, port=7000)