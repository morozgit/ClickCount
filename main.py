import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {
        "Authorization": token
    }
    payload = {
        'long_url': url
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=payload
        )
    response.raise_for_status()
    return response.json()['link']


def split_url(url):
    parsed = urlparse(url)
    return (parsed.netloc + parsed.path)


def count_clicks(token, link):
    headers = {
        "Authorization": token
    }
    clicks_count = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{0}/clicks/summary'.format(link),
        headers=headers
        )
    clicks_count.raise_for_status()
    return clicks_count.json()['total_clicks']


def is_bitlink(token, url):
    headers = {
        "Authorization": token
    }
    response = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{0}'.format(split_url(url)),
        headers=headers
        )
    return response.ok


def main():
    url = input()
    load_dotenv('secret.env')
    token = os.environ['TOKEN']
    try:
        if is_bitlink(token, url):
            clicks_count = count_clicks(token, split_url(url))
            print('click', clicks_count)
        else:
            bit_link = shorten_link(token, url)
            print(bit_link)
    except requests.exceptions.HTTPError as error:
        print('Error is {0}'.format(error))


if __name__ == '__main__':
    main()
