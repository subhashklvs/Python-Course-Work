import re
pattern=r'[0-9]'
res=re.match(pattern,"12 hello world")
print(res.group() if re else "match not found")

# 
pattern=r'h.t'
text='hot hit hut het h@t h*t'
res=re.findall(pattern,text)
print(res)

# 
pattern=r'[aeiou]'
text='cdh2467 cdh3456 cdh5677 cdh4566'
res=re.findall(pattern,text)
print(res)

#
pattern=r'\w'
text='theif@123 12 19 they23 then the the'
res=re.findall(pattern,text)
print(res)
