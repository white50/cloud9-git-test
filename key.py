import requests
import urllib
import json

url = 'https://video-api.unext.jp/api/1/genre_entities?page_number=1&genre_code=TAG0000000240&page_size=5&titles_per_feature=15&entity[]=recommend_blocks&entity[]=live&entity[]=linear_channels'
res = urllib.request.urlopen(url)

data = json.loads(res.read().decode('utf-8'))

for x in data['entities_data']['recommend_blocks']['blocks']:
    for y in x['feature']['titles']:
        print('https://video.unext.jp/title/' + y['title_code'])
        #print(y['title_code'])

#print(data['entities_data']['recommend_blocks']['blocks'][2]['feature']['titles'][1]['title_code'] )
