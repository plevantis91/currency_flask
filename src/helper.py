from src.consts import ACCESS_KEY


def prep_params(from_currency, to_currency, amount):
    # Prepare parameters for the API request
    return {
        'access_key': ACCESS_KEY,
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'format': 1  # Set to 1 for a more human-readable response
    }
