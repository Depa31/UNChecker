# Created by l0gica and TheDepa on 11/26/2018

import requests
import argparse
import time
import threading

parser = argparse.ArgumentParser(description='This script can check if an username is available or occupied on Telegram\n Created by l0gica(github.com/l0gica) and TheDepa(github.com/depa31)')
parser.add_argument('-wl', '-wordlist', required=True, help='Select the wordlist to use')
parser.add_argument('-sv', '-save', help='Save available username in a file')
args=parser.parse_args()

print('Created by l0gica(github.com/l0gica) and TheDepa(github.com/depa31)')
time.sleep(3)

url='https://t.me/'
file=open(args.wl,'r').read().split('\n')
for user in file:
    if len(user)>=5:

        req=requests.get(url+user).text
        if 'tgme_page_title' in req:
            print('[i]The username @'+user+' is occupied')
        else:
            print('[i]The username @'+user+' is available')
            file = open(args.sv,'a').write('@'+user+'\n')

