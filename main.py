import requests
from inputs import *
from audioDownloader import *
from videoDownloader import *

def _select_option_():

    option = input(f'[i] Download\n 1: video\n 2: audio\n :option: ')
    
    if option.isdigit():

        if int(option) == 1:
            video()
        
        if int(option) == 2:
            print('sdf')
            audio()
        

    else:
        print('[-] Wrong Input')
        _select_option_()


def main(URL):
    try:
        req = requests.get(URL)
        if req.status_code == 200:
            print(f'[+] Internet is working and URL is valid.')
            _select_option_()

    except Exception as e:
        print(e)

main(YouTube_URL)