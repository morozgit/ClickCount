import requests

def shorten_link(token, url):
    headers = {
    "Authorization": token
    }
    payload = {
        'long_url': url
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    response.raise_for_status()
    print(response.status_code)
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
    # token = 'bf3030ffa5fb765774f2bb3f493d351487d53092'
    token = '17c09e22ad155405159ca1977542fecf00231da7'
    try:
        bitlink = shorten_link(token, url)
        print('Битлинк',bitlink)
    except requests.exceptions.HTTPError as error:
        exit('Check your link {0}'.format(error))
        # print(error)
    
if __name__ == '__main__':
    main()