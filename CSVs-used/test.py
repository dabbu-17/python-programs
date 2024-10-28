import requests

payload = { 'api_key': 'e5911fe6ec28db5c1f21d576b68fcba6', 'url': 'https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
