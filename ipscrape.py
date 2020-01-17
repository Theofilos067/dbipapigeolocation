#!/usr/bin/env python  

import csv
import requests

FIELDNAMES = (
    'ip',
    'continent_code',
    'country_name',
    'country_capital',
    'countryName',
    'state_prov',
    'city',
    'hostname',
    'organization'
)


def output_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)


def get_location_data(ip_to_check):
    r = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=APIKEY&ip={ip_to_check}')
    r.raise_for_status()
    return r.json()

if __name__ == '__main__':
    with open('file_of_ips.txt', 'r') as f:
        ip_addresses = [line.rstrip() for line in f]

    location_data = [get_location_data(ip) for ip in ip_addresses]
    output_to_csv('location_data.csv', location_data)
