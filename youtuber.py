'''
https://www.youtube.com/results?search_query=smosh
https://www.youtube.com/user/barelypolitical/about
'''

import requests
from bs4 import BeautifulSoup
import argparse


def first_page(name):

    url = 'https://www.youtube.com/results?search_query=' + str(name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    for name in soup.find_all('h3', {'class': 'yt-lockup-title'}, limit=1):
        for user in name.find_all('a'):
            code = user.get('href')
        # return user.get('href')
    main_page(code)


def main_page(idd):
    url = 'https://www.youtube.com' + idd + '/about'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    for stat in soup.find_all('div', {'class': 'about-stats'}):
        print stat.text
        exit(0)
    print "[-]Sorry couldn't find channel"


def main():
    parser = argparse.ArgumentParser(description='Youtuber Info')
    parser.add_argument('channel', type=str, nargs='+',
                        help='Specify Channel Name')
    args = parser.parse_args()
    first_page(args.channel)


if __name__ == '__main__':
    main()
