import json
from urllib.request import urlopen


def usd_rate(source):
    data = json.loads(source)
    return int(data['Valute']['USD']['Value'])

if __name__ == '__main__':
    while True:
        with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
            source = response.read()
        print('input -1 for exit')
        try:
            ch = int(input('input $ count\n'))
            if ch == -1:
                break
            print(usd_rate(source)*ch, 'rub')
        except ValueError as err:
            print('wrong input')
