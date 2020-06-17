from bs4 import BeautifulSoup
import requests as rq

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_image_url(image_code):
    """ Returns image source """
    html = rq.get(f'https://prnt.sc/{image_code}', headers=headers).content
    parsed_html = BeautifulSoup(html)
    img = parsed_html.body.find('img', attrs={'image-id':f'{image_code}'})
    try:
        return img["src"]
    except Exception as e:
        raise FileNotFoundError(f'This happened >> {e}.')
