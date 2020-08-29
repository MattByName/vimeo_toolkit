import unittest
import sys
import vimeo
from decouple import config
import json
import csv

TOKEN = config('VIMEO_TOKEN')
CLIENT_ID = config('VIMEO_CLIENT_ID')
SECRET = config('VIMEO_SECRET')
USER = config('VIMEO_USER',cast=int)

def get_client():
    return vimeo.VimeoClient(
        token='{}'.format(TOKEN),
        key='{}'.format(CLIENT_ID),
        secret='{}'.format(SECRET),
    )

def get_total_pages_from_data(data):
    last_uri = data['paging']['last']
    total_pages = int(last_uri[-1])
    return total_pages

def get_list_of_pages(total, uri):

    uri_list = []
    for x in range(2,total+1):
        uri_list.append(uri+'?page={}'.format(str(x)))
    return uri_list

def get_list_of_all_videos(fields=None):
    client = get_client()
    uri = 'https://api.vimeo.com/me/videos'.format(USER)
    if fields is not None:
        response = client.get(uri,params={"fields": "{}".format(fields)})
    else:
        response = client.get(uri)

    json_data = response.json()
    json_data_set = []

    json_data_set.append(json_data['data'])
    total_pages = get_total_pages_from_data(json_data)

    if total_pages > 1:
        for url in get_list_of_pages(total_pages,uri):
            if fields is not None:
                response = client.get(url, params={"fields": "{}".format(fields)})
            else:
                response = client.get(url)
            page_data = response.json()
            json_data_set.append(page_data['data'])

    rows = []
    for js in json_data_set:
        for jrow in js:

            rows.append([jrow['uri'].lstrip('/videos/'),jrow['name'],jrow['description']])

    return rows

def save_csv(list, fname):

    with open('{}.csv'.format(fname), 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for row in list:
            writer.writerow(row)

def get_vids_csv():
    vid_list = get_list_of_all_videos()
    save_csv(vid_list,'videos')
    return True

def start():
    print("Started")

def init_funcs():
    funcs = {
        "--get-vids-csv": get_vids_csv,
    }
    return funcs


if __name__ == '__main__':
    funcs = init_funcs()
    if sys.argv[1] == "--help":
        for func in funcs:
            print(func)
    elif sys.argv[1] in funcs:
        funcs.get(sys.argv[1])()
    else:
        print('Command not recognised. Try --help')
