from bs4 import BeautifulSoup
import requests as rq

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_image_url(image_code):
    """ Returns image source """
    html = rq.get(f'https://prnt.sc/{image_code}', headers=headers).content
    parsed_html = BeautifulSoup(html, features='lxml')
    img = parsed_html.body.find('img', attrs={'image-id':f'{image_code}'})
    try:
        return img["src"]
    except Exception as e:
        raise FileNotFoundError(f'This happened >> {e}.')


def increment(st):
    """ Algorithm from https://stackoverflow.com/a/20927036/13156017 """
    next_str = ""
    increment = '0'*(len(st)-1) + '1'
    index = len(st) -1
    carry = 0
    curr_digit = 0
    while(index>=0):
        if (st[index].isalpha()):
            curr_digit = (ord(st[index]) + int(increment[index]) + carry)
            if curr_digit > ord('z'):
                curr_digit -= ord('a')
                curr_digit %= 26
                curr_digit += ord('a')
                carry = 1
            else:
                carry = 0
            curr_digit = chr(curr_digit)
            next_str += curr_digit

        elif (st[index].isdigit()):
            curr_digit = int(st[index]) + int(increment[index]) + carry
            if curr_digit > 9:
                curr_digit %= 10
                carry = 1
            else:
                carry = 0
            next_str += str(curr_digit)
        index -= 1
    return next_str[::-1]

