#!/usr/bin/python
import os
import urllib
import urllib2
import argparse
from bs4 import BeautifulSoup


def grabImage(url):
    fromUrl = url
    page = urllib2.urlopen(fromUrl)

    soup = BeautifulSoup(page, 'html.parser')

    pic = soup.find(property="og:image")

    print pic

    imgUrl = pic['content']
    urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'url', type=str, help='instagram url of image')

    args = parser.parse_args()

    grabImage(args.url)
