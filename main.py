import sys
import argparse
import requests
from bs4 import BeautifulSoup
import re


def scraper(url):
    """ scrapes a website for urls, phone numbers and emails."""
    url_list = ['URLS']
    phone_numbers = ['PHONE_NUMBERS']
    emails = []
    r = requests.get(url)
    f = r.text
    
    pn = set(re.findall(
       r"1?([2-9][0-8][0-9][2-9][0-9]{2}[0-9]{4})(\se?x?t?(\d*))?", f))

    urls = re.findall(r'href=[\'"]?([^\'" >]+)', f)

    for email in set(re.findall(
            r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", f)):
        emails.append(email)

    for array in pn:
        for phone_number in array:
            if phone_number != '':
                full_number = (str(phone_number[0:3]) + "-"
                               + str(phone_number[3:6])
                               ) + "-" + str(phone_number[6:10])
                if full_number not in phone_numbers:
                    phone_numbers.append(full_number)
                    print full_number

    for url in urls:
        n = 0
        if 'https' in url:
            n += 1
            if url not in url_list:
                url_list.append(url)

            elif url_list[n - 1] != '...':
                url_list.append('...')

    for url in url_list:
        print(url)

    print('emails')
    print(''.join(emails))


def soup(url):
    r = requests.get(url)
    f = r.text
    soup = BeautifulSoup(f, 'html.parser')
    print "\n HREF urls \n"
    for link in set(soup.find_all('a')):
    
        print(link.get('href'))
    print " \n Img urls \n"
    for link in set(soup.find_all('img')):
        print(link.get('src'))


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '-s', '--scrpfrom',  help='url you will be scraping')
    parser.add_argument('url', help='url')

    return parser


def main(args):
    """Parse args, scan for urls, get images from urls"""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)
    url = parsed_args.url
    if url:
        # scraper(url)
        soup(url)


if __name__ == '__main__':
    main(sys.argv[1:])
