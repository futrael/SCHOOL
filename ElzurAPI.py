import requests

s=requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-GBG')
data = s.json()
k = data["result"][0]["Last"]
print("%.8f" % k)