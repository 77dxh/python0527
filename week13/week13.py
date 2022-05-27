import json
f = open('/Users/a77/python/week13/test2.json','r',encoding='utf-8')
data = json.load(f)
f.close()
print(type(data))
tmp = data ['retVal']

totalvalue = []
for i in tmp:
    totalkey=[]
    tmpvalue=[]
    for key,value in i.items():
        totalkey.append(key)
        tmpvalue.append(value)
    totalvalue.append(tmpvalue)

#  print(totalkey)
#  print(totalvalue)
#print(key + ":" ,end='')
#print(value)

#list generator
totalkey1 = [ key for key , value in tmp[0].items()]
#print(totalkey1)

totalvalue2 = []
for i in tmp:
    tmpvalue2 = [ value for key,value in i.items()]
    totalvalue2.append(tmpvalue2)

#print(len(totalvalue2))
# print(totalkey)
tmpheader = ','.join(totalkey)
# print(tmpheader)

tmpvalue=''
for i in totalvalue:
    tmp = ','.join([str(k) for k in i])+'\n'
    tmpvalue = tmpvalue+tmp
print(tmpvalue)


kk = open('test3.csv','w',encoding='utf-8')
kk.write(tmpheader)
kk.write(tmpvalue)
kk.close()