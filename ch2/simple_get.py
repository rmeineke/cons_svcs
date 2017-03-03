import requests


def main():
    url = 'https://talkpython.fm'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Error fetching page: {}'.format(resp.status_code))

    print(resp.text[:500])


if __name__ == '__main__':
    main()

