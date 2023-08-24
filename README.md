# KrakenFlex-Backend-Test

This is a small program that utilizes KrakenFlex API as a part of the test for KrakenFlex. The purpose of the program is to:

1. Retrieve all outages from the `GET /outages` endpoint.
2. Retrieve information from the `GET /site-info/{siteId}` endpoint for the site with the given ID.
3. Filter out any outages that began before `2022-01-01T00:00:00.000Z` or don't have an ID that is in the list of
   devices in the site information.
4. For the remaining outages, attach the name of the device.
5. Send the filtered list of outages to `POST /site-outages/{siteId}`

## Hot to run

Clone the repository
In the repository:
Setup virutal environment:
python -m venv krakenflex_venv
Install dependencies:
pip install -r requirements.txt

python main.py

## Testing

There are unit tests in this project. To run tests using command:

python -m unittest test_outages.py
