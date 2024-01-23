from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Your ExchangeRate API access key
access_key = '219724147fdff6296ab90e010b04310e'

# ExchangeRate API endpoint for conversion
convert_endpoint = 'http://api.exchangerate.host/convert'

# Flask route for the home page
@app.route('/', methods=['GET', 'POST'])
def forex_converter():
    if request.method == 'POST':
        # Get form data
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        # Perform currency conversion
        conversion_result = perform_conversion(from_currency, to_currency, amount)

        return render_template('result.html', result=True,
                               from_currency=from_currency, to_currency=to_currency,
                               amount=amount, conversion_result=conversion_result)

    # Render the initial form
    return render_template('index.html', result=False)

def perform_conversion(from_currency, to_currency, amount):
    # Prepare parameters for the API request
    params = {
        'access_key': access_key,
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'format': 1  # Set to 1 for a more human-readable response
    }

    # Make the API request
    response = requests.get(convert_endpoint, params=params)
    data = response.json()

    # Check if the request was successful
    if data.get('success', False):
        return data['result']
    else:
        return f"Conversion failed. Error: {data.get('error', 'Unknown error')}"

if __name__ == '__main__':
    app.run(debug=True)



