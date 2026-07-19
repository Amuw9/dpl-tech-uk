import requests

from config.config import API_URL, API_PARAMS


def fetch_api_data():

    response = requests.get(API_URL, params=API_PARAMS)

    response.raise_for_status()

    json_response = response.json()

    return [row["attributes"] for row in json_response["features"]]