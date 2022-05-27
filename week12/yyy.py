from urllib import response
import requests
import json

data = {'lang':'tw','type':'2'}
response = requests.get("http://apis.youbike.com.tw/api/front/station/all",params=data)
if response.status_code == 200:
    kk = response.content.decode('utf-8')

    tmp = json.loads(kk)
    f = open("test2.json","wb")

    kk1 = json.dumps(tmp,indent=4,ensure_ascii=False).encode('utf-8')
    f.write(kk1)
    f.close()
    


