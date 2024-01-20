from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = '219724147fdff6296ab90e010b04310e'
BASE_URL = 'http://api.exchangerate.host/live?access_key=219724147fdff6296ab90e010b04310e'

def get_exchange_rates(base_currency='USD'):
    params = {'base': base_currency, 'symbols': ''}
    response = request.get(BASE_URL, params=params)
    data = response.json
    return data['rates']

@app.route('/')
def index():
    # Get the list of currencies for the dropdown
    currencies = get_exchange_rates().keys()
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    # Retrieve data from the form
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    # Fetch the latest exchange rates
    exchange_rates = get_exchange_rates(from_currency)

    # Perform the conversion
    if to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[to_currency]
        result = {'success': True, 'converted_amount': converted_amount}
    else:
        result = {'success': False, 'error': 'Invalid currency code'}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)