lst=["t","r","rt","s"]
lst.insert(1,"e")
print(lst)

print(lst.pop(2))
print(lst)

lst1=["1","2","3","5"]
lst2=["cat","dog","pig","monkey","dockey"]
t=zip(lst1,lst2)
print(t)
d=dict(t)
print(d)

d=dict(cat=10,dog=20)
print(d,"max:",max(d))

d={"hello":10,"python":20,"world":30}
print(d["hello"])
print(d.get("hello"))

for item in d.items():
    print(item)

lst1=[11,12,13,14,15]
lst2=["CYY","SCC","XLL","XHH","GYY"]
d=dict(zip(lst1,lst2))
print(d)

lst1=[11,12,13,14,15]
lst2=["CYY","SCC","XLL","XHH","GYY"]
d={}
for key,value in zip(lst1,lst2):
    d[key]=value
print(d)