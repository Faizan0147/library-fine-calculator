# Library Fine Calculator

Small Flask web form: enter days a book is overdue (integer 0-30). First 3 days are free,
then Rs 10 per day. Values outside 0-30 or non-integers are rejected.
Used for Software Engineering Lab 12/13 (AI-assisted code review + Selenium testing).

## Run
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000/

## Test
```
python -m pytest                 # unit tests
python tests/test_selenium.py    # browser tests (app must be running, Chrome required)
```
