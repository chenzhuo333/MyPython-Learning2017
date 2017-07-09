a = "7654321"
b= "1234567"
print zip(a,b)

e=[]
for c,d in zip(a,b):
    f=int(c)+int(d)
#    print f
    e.append(f)
    
print e
#print list(zip(a,b))


lst=['a','b','c','d','e']

myiter=iter(lst)

myiter.next()