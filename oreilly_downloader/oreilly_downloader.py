#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Downloads the free ebooks offered by O'Reilly. They can be downloaded by
categories in different formats.

Author: Alberto Martinez de Murga (@threkk)
License: MIT
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import argparse
import re
import sys
# https://www.reddit.com/r/Python/comments/56syaa/7_oreilly_python_books_for_free/
# https://github.com/travis-ci/travis-ci/issues/3747
# http://docopt.org/
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import URLError

CATEGORIES = ['programming', 'business', 'data', 'iot', 'security',
              'web-platform', 'webops-perf']


def scrape_site(category):
    """
    Retrieves all the books within a category.

    :param category: str Category.
    :return list All the books in the category.
    """
    url = 'http://www.oreilly.com/{category}/free/'.format(category=category)

    try:
        req = urlopen(url)
    except URLError:
        print('OReilly\'s website is not reacheable at the moment')
        sys.exit()

    html = req.read().decode('utf-8')

    regexp = re.compile(r'{url}.+\.csp'.format(url=url))
    unique_books_url = list(set(regexp.findall(html)))

    return unique_books_url


def download_book(book_url, epub, mobi, pdf):
    """
    Downloads a book in the given format. The book is downloaded in the current
    directory.

    :param book_url: string Book
    :param epub: bool If true, the book will be downloaded in epub format.
    :param mobi: bool If true, the book will be downloaded in mobi format.
    :param pdf: bool If true, the book will be downloaded in pdf format.
    """
    if (epub or mobi or pdf) is False:
        print('Please, specify at least one format to download the books.')
        sys.exit()

    book_url = book_url.replace('/free/', '/free/files/')
    if epub:
        epub_url = book_url.replace('.csp', '.epub')
        local_epub = epub_url.split('/')[-1]
        try:
            urlretrieve(epub_url, local_epub)
            print('[·] Downloaded {name}'.format(name=local_epub))
        except URLError:
            print('[x] Error downloading {name}'.format(name=local_epub))

    if mobi:
        mobi_url = book_url.replace('.csp', '.mobi')
        local_mobi = mobi_url.split('/')[-1]
        try:
            urlretrieve(mobi_url, local_mobi)
            print('[·] Downloaded {name}'.format(name=local_mobi))
        except URLError:
            print('[x] Error downloading {name}'.format(name=local_mobi))

    if pdf:
        pdf_url = book_url.replace('.csp', '.pdf')
        local_pdf = pdf_url.split('/')[-1]
        try:
            urlretrieve(pdf_url, local_pdf)
            print('[·] Downloaded {name}'.format(name=local_pdf))
        except URLError:
            print('[x] Error downloading {name}'.format(name=local_pdf))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description=r'Downloads the free ebooks '
                                     r'offered by OReilly. They can be '
                                     r'downloaded by categories in different '
                                     r'formats.')

    PARSER.add_argument('category',
                        metavar='<category>',
                        type=str,
                        choices=CATEGORIES,
                        nargs='*',
                        help=r'category of the books. Choose between: ' +
                        r' '.join(CATEGORIES))

    PARSER.add_argument('-e', '--epub', action='store_true',
                        help=r'download the book in ePub format.')
    PARSER.add_argument('-m', '--mobi', action='store_true',
                        help=r'download the book in Mobi format.')
    PARSER.add_argument('-p', '--pdf', action='store_true',
                        help=r'download the book in PDF format.')

    PARSER.add_argument('-v', '--version', action='version', version='1.0')

    ARGS = PARSER.parse_args()

    for category in ARGS.category:
        print('==> Retrieving {category} books'.format(category=category))
        book_urls = scrape_site(category)

        for book_url in book_urls:
            download_book(book_url, ARGS.epub, ARGS.mobi, ARGS.pdf)
