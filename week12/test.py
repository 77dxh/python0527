
from tokenize import group


class Person : 
    def __init__(self,name,age,hight,weight) :
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight

group = []
       
f = open('/Users/a77/python/week12/test1.csv','r',encoding='utf-8')
result = f.readlines()
print(result)
for i in result:
    tmp = i.split(',')
    name = tmp[0]
    age = int(tmp[1])
    hight = tmp[2]
    weight = tmp[3].split('\n')[0]
    kk = Person(name,age,int(hight),int(weight))
    group.append(kk)
    #print(name+age+hight+weight)
    #print(i.split(','))
#for i in result:
#   print(i)
f.close()






class Transaction:
    def __init__(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

f = open('/Users/a77/Downloads/covid19.csv','r',encoding='utf-8')
result = f.readlines()
header = result[0]
result.pop(0)
record = []
for i in result:
    tmp = i.split('\n')[0].split(',')
    print(tmp)
    通報日 = tmp[0]
    法定傳染病通報 = float(tmp[1])
    居家檢疫送驗 = float(tmp[2])
    擴大檢測送驗 = float(tmp[3])
    Total = float(tmp[4])
    kk = Transaction(通報日,法定傳染病通報,居家檢疫送驗,擴大檢測送驗,Total)
    record.append(kk)
f.close()
