#!/usr/bin/env python

import csv

import requests  # third-party, pip install requests

FIELDNAMES = (
    'ipAddress',
    'continentCode',
    'continentName',
    'countryCode',
    'countryName',
    'stateProv',
    'city'
)


def output_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)


def get_location_data(ip_to_check):
    r = requests.get('https://api.ipgeolocation.io/ipgeo-bulk?apiKey=APIKEY'.format(ip_to_check))
    r.raise_for_status()
    return r.json()

if __name__ == '__main__':
    with open('file_of_ips.txt', 'r') as f:
        ip_addresses = [line.rstrip() for line in f]

    location_data = [get_location_data(ip) for ip in ip_addresses]
    output_to_csv('location_data.csv', location_data)

# for hardcoding ip addresses to script
#
#if __name__ == '__main__':
#    ip_addresses = [
#        '172.217.3.206',   # google.com
#        '204.79.197.200',  # bing.com
#        '17.178.96.59',    # apple.com
#        '104.36.192.183'   # uber.com
#    ]
#    location_data = [get_location_data(ip) for ip in ip_addresses]
#    output_to_csv('location_data.csv', location_data)
