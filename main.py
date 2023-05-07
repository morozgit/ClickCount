import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv, find_dotenv
import argparse


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
    url_parts = urlparse(url)
    return '{0}{1}'.format(url_parts.netloc, url_parts.path) 


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
    url = argparse.ArgumentParser(
            description='''You are able to make a short link or
                            count clicks on it'''
        )
    url.add_argument('link', help='Enter link ')
    args = url.parse_args()
    load_dotenv(find_dotenv())
    token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(token, args.link):
            clicks_count = count_clicks(token, split_url(args.link))
            print('click', clicks_count)
        else:
            bit_link = shorten_link(token, args.link)
            print(bit_link)
    except requests.exceptions.HTTPError as error:
        print('Error is {0}'.format(error))


if __name__ == '__main__':
    main()
