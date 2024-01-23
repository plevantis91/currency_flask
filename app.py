from flask import Flask, render_template, request
import requests

from src.consts import ACCESS_KEY, CONVERT_ENDPOINT
from helper import prep_params

app = Flask(__name__)

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
    params = prep_params(from_currency, to_currency, amount)

    # Make the API request
    response = requests.get(CONVERT_ENDPOINT, params=params)
    data = response.json()

    # Check if the request was successful
    if data.get('success', False):
        return data['result']
    return f"Conversion failed. Error: {data.get('error', 'Unknown error')}"

if __name__ == '__main__':
    app.run(debug=True)



