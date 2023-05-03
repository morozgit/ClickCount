import requests
from urllib.parse import urlparse


def shorten_link(token, url):
    headers = {
    "Authorization": token
    }
    payload = {
        'long_url': url
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    response.raise_for_status()
    # print(response.status_code)
    return response.json()['link']


def count_clicks(token, link):
    headers = {
    "Authorization": token
    }
    # payload = {
    #     'long_url': link
    # }
    clicks_count = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{0}/clicks/summary'.format(link), headers=headers)
    clicks_count.raise_for_status()
    # print(response.status_code)   
    return clicks_count


def main():
    # url = 'https://api-ssl.bitly.com/v4/user'
    # headers = {
    # "Authorization": "bf3030ffa5fb765774f2bb3f493d351487d53092"
    # }
    # response = requests.get(url, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    url = input()
    # token = 'bf3030ffa5fb765774f2bb3f493d351487d53092'
    token = '17c09e22ad155405159ca1977542fecf00231da7'
    try:
        bit_link = shorten_link(token, url)
        print(bit_link)
        clicks_count = count_clicks(token, bit_link)
        print(clicks_count)
    except requests.exceptions.HTTPError as error:
        print('Error is {0}'.format(error))
        

if __name__ == '__main__':
    main()
    