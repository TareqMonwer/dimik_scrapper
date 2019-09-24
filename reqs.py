import os
import requests as req
import webbrowser as wb

uri = 'http://subeen.com/প্রোগ্রামিং-চর্চার-১০টি/'
res = req.get(uri)

with open('subeen.com_10judges.html', 'w', encoding=res.encoding) as file:
    file.write(res.text)

file_path = os.path.realpath('subeen.com_10judges.html')
print(file_path)
wb.open('file://' + file_path)