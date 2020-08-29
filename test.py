import unittest
import vimeo
from decouple import config
import json
from base import get_list_of_all_videos, get_total_pages_from_data, get_list_of_vid_ids

TOTAL_VIDEOS=65 #required for tests to work, you'll need to manually enter how many videos you have.
TOKEN = config('VIMEO_TOKEN')
CLIENT_ID = config('VIMEO_CLIENT_ID')
SECRET = config('VIMEO_SECRET')
USER = config('VIMEO_USER',cast=int)

class VimeoApiTest(unittest.TestCase):

    def test_can_connect_to_api(self):

        client = vimeo.VimeoClient(
            token='{}'.format(TOKEN),
            key='{}'.format(CLIENT_ID),
            secret='{}'.format(SECRET),
        )
        uri = 'https://api.vimeo.com'
        response = client.get(uri)

        self.assertEqual(response.status_code,200)

    def test_can_retrieve_accurate_videos_number(self):

            client = vimeo.VimeoClient(
                token='{}'.format(TOKEN),
                key='{}'.format(CLIENT_ID),
                secret='{}'.format(SECRET),
            )
            uri = 'https://api.vimeo.com/users/{}/videos'.format(USER)
            response = client.get(uri)
            json_response = response.json()
            self.assertEqual(json_response['total'],TOTAL_VIDEOS)

    def test_get_list_of_vids_gets_right_number(self):

        client = vimeo.VimeoClient(
            token='{}'.format(TOKEN),
            key='{}'.format(CLIENT_ID),
            secret='{}'.format(SECRET),
        )
        uri = 'https://api.vimeo.com/users/{}/videos'.format(USER)
        response = client.get(uri)
        json_response = response.json()
        total_videos = int(json_response['total'])

        self.assertEqual(total_videos,len(get_list_of_all_videos()))

    def test_get_list_list_of_ids_gets_right_number(self):
        client = vimeo.VimeoClient(
            token='{}'.format(TOKEN),
            key='{}'.format(CLIENT_ID),
            secret='{}'.format(SECRET),
        )
        uri = 'https://api.vimeo.com/users/{}/videos'.format(USER)
        response = client.get(uri)
        json_response = response.json()
        total_videos = int(json_response['total'])

        self.assertEqual(total_videos,len(get_list_of_vid_ids()))

    def test_get_total_pages_gets_accurate_pages(self):
        test_total_pages = 3
        client = vimeo.VimeoClient(
            token='{}'.format(TOKEN),
            key='{}'.format(CLIENT_ID),
            secret='{}'.format(SECRET),
        )
        uri = 'https://api.vimeo.com/users/{}/videos'.format(USER)
        response = client.get(uri)
        json_response = response.json()
        self.assertEqual(test_total_pages, get_total_pages_from_data(json_response))







if __name__ == '__main__':
    unittest.main()
    CLIENT_ID = config('VIMEO_CLIENT_ID')
    SECRET = config('VIMEO_SECRET')
    client = vimeo.VimeoClient(
        key='{}'.format(CLIENT_ID),
        secret='{}'.format(SECRET),
    )

