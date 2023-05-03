import requests

def shorten_link(token, url):
    headers = {
    "token": token
    }
    payload = {
        'long_url': url
    }

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    response.raise_for_status()

    # print("short url", response.json()['link'])

def main():
    # url = 'https://api-ssl.bitly.com/v4/user'
    # headers = {
    # "Authorization": "bf3030ffa5fb765774f2bb3f493d351487d53092"
    # }
    # response = requests.get(url, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    url ='https://www.google.com'
    token = 'bf3030ffa5fb765774f2bb3f493d351487d53092'
    print('Битлинк', shorten_link(token, url))



if __name__ == '__main__':
    main()