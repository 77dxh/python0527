import pandas as pd
import json

data = pd.Series([80,90,50,30],index=['國文','英文','數學','社會'])
print(data)
#print(data['國文'])
print(data['英文':'社會'])


data1 = pd.Series([80,90,50,30])

print(data1)
print(data[1])

#print(data.index)
#print(data.values)

#dataframe
grade_python = pd.Series({'c101':80,'c102':90,'c103':50,'c104':30})
print(grade_python)
grade_php = pd.Series({'c101':100,'c102':80,'c103':90,'c104':60})
print(grade_php)
grade_cal = pd.Series({'c101':70,'c102':90,'c103':40,'c104':20})
grade_total = pd.DataFrame({'python':grade_python,'程式設計':grade_php,'微積分':grade_cal})
print(grade_total)

print(grade_total.index)
print(grade_total.values)
print(grade_total.columns)
print(grade_total.shape)

f = open('test2.json','r',encoding='utf-8')
# strng --> dict
data = json.load(f)
f.close()

tmp = data ['retVal']
df = pd.DataFrame(tmp)

print(df)
print(df.shape)
print(df.values)

df.to_csv("123.csv",index=False,header=False)
df.to_excel("www.xls")