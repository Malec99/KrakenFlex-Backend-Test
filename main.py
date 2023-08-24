from endpoints import get_all_outages, get_site_info, update_outages
from utils import filter_outages

SITE_ID = "norwich-pear-tree"


def main():
    outages = get_all_outages()

    site_info = get_site_info(SITE_ID)

    filtered_outages = filter_outages(outages, site_info)

    response = update_outages(SITE_ID, filtered_outages)
    if response.status_code == 200:
        print("Outages sent successfully.")
    else:
        print("Error: " + response.json()["message"])


if __name__ == "__main__":
    main()
