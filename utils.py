from datetime import datetime
import time
from http import HTTPStatus
from http.client import HTTPException


def filter_outages(outages, site_info):
    filtered_outages = []
    earliestDate = "2022-01-01T00:00:00.000Z"
    for outage in outages:
        start_date = datetime.fromisoformat(outage["begin"])
        if start_date >= datetime.fromisoformat(earliestDate):
            device_ids = [device["id"] for device in site_info["devices"]]
            if outage["id"] in device_ids:
                try:
                    device_name = next(
                        device["name"]
                        for device in site_info["devices"]
                        if device["id"] == outage["id"]
                    )
                except StopIteration:
                    continue
                else:
                    outage["name"] = device_name
                    filtered_outages.append(outage)
    return filtered_outages


def retry_request(max_retries, request_func, *args, **kwargs):
    for retry in range(max_retries):
        response = request_func(*args, **kwargs)

        if response.status_code == 500:
            time.sleep(1)
        else:
            return response

    raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR)
