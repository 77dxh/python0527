import json
import pandas as pd

f = open('test2.json','r',encoding='utf-8')
# strng --> dict
data = json.load(f)
f.close()

tmp = data ['retVal']
df = pd.DataFrame(tmp)

print(df)