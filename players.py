import re


with open('players.html') as file:
    text = file.read()

print(re.findall(r'<li>(\w+)', text))