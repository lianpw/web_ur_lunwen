import json

with open('./temps/cookies/cookies.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data, type(data))

    # data2 = json.load(f)
    # print(data2, type(data2))

l = [{'domain': '127.0.0.1', 'httpOnly': False, 'name': 'is_distribut', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'user_id', 'path': '/', 'secure': False, 'value': '2593'}, {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'onrijco03jucp0sofffejtlf24'}, {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'uname', 'path': '/', 'secure': False, 'value': '18513087182'}, {'domain': '127.0.0.1', 'expiry': 1663755842, 'httpOnly': False, 'name': 'is_mobile', 'path': '/', 'secure': False, 'value': '0'}]

