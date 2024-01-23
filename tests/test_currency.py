from unittest import TestCase

from src import currency
from src import app


app.config["TESTING"] = True

app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class CurrencyTests(TestCase):
    """integration tests for the app"""

    def test_do_request(self):
        with app.test_client() as client:
            resp = client.get("/home")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            

