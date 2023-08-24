import requests
import json

from utils import retry_request

BASE_URL = "https://api.krakenflex.systems/interview-tests-mock-api/v1"

API_KEY = open("api-key.txt", "r").readline().strip()

SITE_ID = "norwich-pear-tree"


def get_all_outages():
    url = BASE_URL + "/outages"
    headers = {"x-api-key": API_KEY}
    response = retry_request(3, requests.get, url, headers=headers)

    return response.json()


def get_site_info(site_id):
    url = BASE_URL + "/site-info/" + site_id
    headers = {"x-api-key": API_KEY}
    response = retry_request(3, requests.get, url, headers=headers)

    return response.json()


def update_outages(site_id, outages):
    url = BASE_URL + "/site-outages/" + site_id
    headers = {"x-api-key": API_KEY}
    payload = json.dumps(outages)
    response = retry_request(3, requests.post, url, headers=headers, data=payload)

    return response
