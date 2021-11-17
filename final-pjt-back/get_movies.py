from tmdb import TMDBHelper
import requests
import pandas as pd


tmdb_helper = TMDBHelper('043ba4036363b1f15534a85a719d4706')

for i in range(1, 51):
    request_url = tmdb_helper.get_request_url(language='ko-KR', page=str(i))
    data = requests.get(request_url).json()
    df = pd.json_normalize(data['results'])
    if i == 1:
        info = df
    else:
        info = info.append(df, ignore_index=True)

info.to_csv("data.csv", header=False)

# with open("data.json", "w", encoding='UTF8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)