import json
import requests
import os
from datetime import date, timedelta

src_base_path = f"//db-rb-fs001/data_qlik_desktop/data_source_apps/customer_alliance_V2/"
base_url = "https://api.customer-alliance.com/statistics/v2/portal-overview.json?"

api_keys = []

with open(f"{src_base_path}/API_Keys/CustomerAlliance_API_H-Hotels.txt", "r") as file:
    for line in file:
        api_keys.append(line.strip())

this_month_start = date.today().replace(day=1)
this_month_end = (date.today().replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
last_month_end = this_month_start - timedelta(days=1)
last_month_start = last_month_end.replace(day=1)

if os.path.exists(f"{src_base_path}/portal_rating/Portal_Data_{this_month_start}-{this_month_end}.txt"):
    os.remove(f"{src_base_path}/portal_rating/Portal_Data_{this_month_start}-{this_month_end}.txt")
else:
    print("No existing actual data file.")

if os.path.exists(f"{src_base_path}/portal_rating/Portal_Data_{last_month_start}-{last_month_end}.txt"):
    os.remove(f"{src_base_path}/portal_rating/Portal_Data_{last_month_start}-{last_month_end}.txt")
else:
    print("No existing last month data file.")


def get_portal_data(api_key):
    headers = {'X-CA-AUTH': api_key}
    api_url = base_url + add_url
    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.headers)
    if response.status_code == 200:
        global data
        data = json.loads(response.text)
        return data


for api_key in api_keys:
    add_url = f"start={this_month_start}&end={this_month_end}"
    get_portal_data(api_key)

    portal_names = []

    for key in data['portalStats']:
        portal_names.append(key)

    for portal_name in portal_names:
        try:
            portal_detail = data['portalStats'][portal_name]
            # print(data['portalStats'][portal_name])
            review_count = (portal_detail['reviewCount'])
            review_rating_weighted = (portal_detail['averageRating']) * review_count
            with open("Portal_Data_" + str(startdyn) + "-" + str(enddyn) + ".txt", "a") as file:
                file.write(str(api_token) + ',' + str(startdyn) + ',' + str(enddyn) + ',' + str(portal_name) + ',' + str(review_count) + ',' + str(review_rating_weighted) + "\n")
            print(str(api_token) + ',' + str(startdyn) + ',' + str(enddyn) + ',' + str(portal_name) + ',' + str(review_count) + ',' + str(review_rating_weighted))
        except KeyError:
            pass

for api_token in api_tokens:
    add_url = "start=" + str(start_last_dyn) + "&end=" + str(end_last_dyn)
    pull_data(api_token)

    portal_names = []

    for key in data['portalStats']:
        portal_names.append(key)
        # print(portal_names)

    for portal_name in portal_names:
        try:
            portal_detail = data['portalStats'][portal_name]
            # print(data['portalStats'][portal_name])
            review_count = (portal_detail['reviewCount'])
            review_rating_weighted = (portal_detail['averageRating']) * review_count
            with open("Portal_Data_" + str(start_last_dyn) + "-" + str(end_last_dyn) + ".txt", "a") as file:
                file.write(str(api_token) + ',' + str(start_last_dyn) + ',' + str(end_last_dyn) + ',' + str(portal_name) + ',' + str(review_count) + ',' + str(review_rating_weighted) + "\n")
            print(str(api_token) + ',' + str(start_last_dyn) + ',' + str(end_last_dyn) + ',' + str(portal_name) + ',' + str(review_count) + ',' + str(review_rating_weighted))
        except KeyError:
            pass