import json
import requests


token = '55fcf42cb0b14618a8d658476b672f99'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'OAuth ' + token}


def create_folder(folder_name):
    params = {'path': folder_name}
    result = requests.put(url, headers=headers, params=params)
    return result.status_code
