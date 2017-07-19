# coding=utf8

s = 'mysa.afasdf.werewar.adfasdf.aaaa'

print s.split('.')

ss =['mysa', 'afasdf', 'werewar', 'adfasdf', 'aaaa']

print ','.join(ss)

sss ={'1':'mysa','2': 'afasdf', '3':'werewar', '4':'adfasdf', '5':'aaaa'}

list = []
for mys in sss:
#     print mys

    list.append(sss[mys])
#     print ';'.join(sss[mys])
print ';'.join(list)

list1 = []
for mys in sss.values():
    list1.append(mys)
print ';'.join(list1)