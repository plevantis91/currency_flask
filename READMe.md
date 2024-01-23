python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install Flask
pip freeze > requirement.txt
flask --app hello run