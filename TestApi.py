import requests
import pytest
import json


class Initialization:
    base_url = 'https://sellermetrix.com/api/v2/cached-reports/'
    JWTtoken = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InBlcm9sYS5lcmljc3NvbkBnbWFpbC5jb2" \
               "0iLCJpYXQiOjE2NDQyOTkxMzgsImV4cCI6MTY0Njg5MTEzOCwianRpIjoiNDUwYTMyZGUtMTVkNi00NjI4LTkzMDct" \
               "YzFkZjQ0MGRlNDAwIiwidXNlcl9pZCI6MTUsInVzZXJfcHJvZmlsZV9pZCI6WzEzXSwib3JpZ19pYXQiOjE2NDQyOTk" \
               "xMzh9.FxLSD2CWgGePZ1a-kpm6-QBM2spUV85UPiGSN8fVG-I"
    headersauthorized = {
        "Authorization": JWTtoken
    }
    reports = 0
    datapost = {
        "type": "profit-and-loss",
        "marketplace_id": 3,
        "brandIds": "",
        "productIds": "",
        "parentIds": "",
        "name": "Name",
        "from": "2021-11-01",
        "to": "2021-11-30"
    }
    datatup = [
        {
            "id": 266,
            "name": "Name",
            "marketplace_id": 3,
            "start": "2021-03-01",
            "end": "2021-03-31",
            "status": "in_progress",
            "type": "profit-and-loss",
            "request_date": "2021-12-20T13:41:00.944006Z"
        },
        {
            "id": 264,
            "name": "P&L Report 1-16 Dec",
            "marketplace_id": 3,
            "start": "2021-12-01",
            "end": "2021-12-16",
            "status": "completed",
            "type": "profit-and-loss",
            "request_date": "2021-12-17T12:37:13.685248Z"
        }
    ]


class TestRequest:
    def test_first_api_post(self):
        first_response = requests.post(Initialization.base_url, data=Initialization.datapost,
                                       headers=Initialization.headersauthorized)
        print(first_response.status_code)
        print("______________________________________________________________________________")

    @pytest.mark.parametrize("dataparam", Initialization.datatup)
    def test_second_api_get(self, dataparam):
        second_response = requests.get(Initialization.base_url, params=dataparam,
                                       headers=Initialization.headersauthorized)
        print(second_response.json())
        print(dataparam)
        for i in second_response.json():
            print(i)
            if i['end'] == dataparam['end']:
                print(i)
                if i['name'] == 'Profit & Loss':
                    print(i)
                    Initialization.reports = i['id']
                    print(Initialization.reports)

        print(second_response.status_code)
        print("______________________________________________________________________________")

    @pytest.mark.parametrize("dataparam", Initialization.datatup)
    def test_third_api_get(self, dataparam):
        url_download = Initialization.base_url + str(Initialization.reports)
        third_response = requests.get(url_download, params=dataparam,
                                      headers=Initialization.headersauthorized)
        print(third_response.json())
        myfile = open("Reports.json", "w+")
        myfile.write(json.dumps(third_response.json()))
