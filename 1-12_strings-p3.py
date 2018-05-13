from __future__ import print_function, unicode_literals

my_str1 = 'whatever' #quote types can be single or double but need to match
my_str2 = "something else"
my_str3 = '''This is a string
that spans
multiple lines
''' #using 3 quotes lets you use multiple lines.

print(my_str1)
print(my_str2)
print(my_str3)

print(repr(my_str3)) #print representation of string 3, ie what it looks like internally to python
