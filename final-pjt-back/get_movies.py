import requests, json
from tmdb import TMDBHelper


tmdb_helper = TMDBHelper('043ba4036363b1f15534a85a719d4706')
request_url = tmdb_helper.get_request_url(language='ko-KR', page='2')
data = requests.get(request_url).json()

with open("data.json", "w", encoding='UTF8') as f:
    json.dump(data, f, ensure_ascii=False)