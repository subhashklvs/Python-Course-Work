import re
pattern=r'[0-9]'
res=re.match(pattern,"12 hello world")
print(res.group() if re else "match not found")