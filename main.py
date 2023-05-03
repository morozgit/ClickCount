import requests

def shorten_link(token, url):
    headers = {
    "Authorization": token
    }
    payload = {
        'long_url': url
    }

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    print(response.raise_for_status())
    return response.json()['link']

def main():
    # url = 'https://api-ssl.bitly.com/v4/user'
    # headers = {
    # "Authorization": "bf3030ffa5fb765774f2bb3f493d351487d53092"
    # }
    # response = requests.get(url, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    url = input()
    token = 'bf3030ffa5fb765774f2bb3f493d351487d53092'
    try:
        print('Битлинк', shorten_link(token, url))
    except requests.exceptions.HTTPError as error:
        exit('Check your link, error {error}'.format(error))


if __name__ == '__main__':
    main()