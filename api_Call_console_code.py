Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as url
>>> url.urlopen('https://api.covid19india.org/states_daily.json')
<http.client.HTTPResponse object at 0x0000024EAF8D0250>
>>> response = url.urlopen('https://api.covid19india.org/states_daily.json')
>>> import json
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> states = data['states_daily']
>>> type(states)
<class 'list'>
>>> states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
>>> states[-1]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '1', 'ch': '0', 'ct': '1', 'date': '06-Mar-21', 'dateymd': '2021-03-06', 'dd': '0', 'dl': '1', 'dn': '0', 'ga': '0', 'gj': '1', 'hp': '0', 'hr': '3', 'jh': '0', 'jk': '1', 'ka': '5', 'kl': '16', 'la': '0', 'ld': '0', 'mh': '47', 'ml': '0', 'mn': '0', 'mp': '2', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '12', 'py': '0', 'rj': '0', 'sk': '0', 'status': 'Deceased', 'tg': '1', 'tn': '4', 'tr': '0', 'tt': '98', 'un': '0', 'up': '0', 'ut': '0', 'wb': '2'}
>>> res = url.urlopen('https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=35320')
>>> data = json.load(res)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['pid', 'profile', 'imageURL', 'battingStyle', 'bowlingStyle', 'majorTeams', 'currentAge', 'born', 'fullName', 'name', 'country', 'playingRole', 'v', 'data', 'ttl', 'provider', 'creditsLeft'])
>>> data['profile']
"\n\nSachin Tendulkar has been the most complete batsman of his time, the most prolific runmaker of all time, and arguably the biggest cricket icon the game has ever known. His batting was based on the purest principles: perfect balance, economy of movement, precision in stroke-making, and that intangible quality given only to geniuses - anticipation. If he didn't have a signature stroke - the upright, back-foot punch comes close - it's because he was equally proficient at each of the full range of orthodox shots (and plenty of improvised ones as well) and can pull them out at will.  \n\n"
>>> 