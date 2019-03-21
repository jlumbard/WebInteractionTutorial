import requests
sesh = requests.session()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/wine-14/00-pouilly-fuisse-la-frairie-799833-1"

sesh.get(url, headers = headers)


