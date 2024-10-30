#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description='Extract links from provided URLs.')
    parser.add_argument('-u', '--url', action='append', required=True, help='URL to extract links from.')
    parser.add_argument('-o', '--output', choices=['stdout', 'json'], required=True, help='Output format.')
    return parser.parse_args()

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {url}: {e}')
        return ''

def extract_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        absolute_url = urljoin(base_url, href)
        links.add(absolute_url)
    return links

def process_urls(urls):
    result = {}
    for url in urls:
        html_content = fetch_html(url)
        links = extract_links(html_content, url)
        result[url] = links
    return result

def output_results(results, output_format):
    if output_format == 'stdout':
        for url, links in results.items():
            for link in links:
                print(link)
    elif output_format == 'json':
        json_output = {}
        for url, links in results.items():
            domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
            paths = [urlparse(link).path or '/' for link in links]
            json_output[domain] = list(set(paths))
        print(json.dumps(json_output, indent=4))

def main():
    args = parse_arguments()
    results = process_urls(args.url)
    output_results(results, args.output)

if __name__ == '__main__':
    main()
    while True:
        time.sleep(3600)
