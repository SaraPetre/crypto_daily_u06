from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = {
    "id": "1,1027"
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e31d4fce-390c-4787-87aa-fec1b76c1d93',
}

session = Session()
session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   data = [{"symbol": d[0]} for d in data]
#   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)


try: 
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)    