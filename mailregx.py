import re

text = 'email me here: tareq@me.com or tareq@m e.com'
result = re.findall(r'(\w+@\w+\.\w+)', text)
print(result)