class a:

    __slots__="class a"
    

print a.__slots__

a.__slots__="new a"

print a.__slots__


b = a()
b.__slots__="new b"

print b.__slots__