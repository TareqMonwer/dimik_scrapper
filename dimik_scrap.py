import os
import re
import sys
import requests


def create_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        # print(name, 'already exists')
        return name

url = 'http://dimik.pub'
response = requests.get(url)
if not response.ok:
    sys.exit('Could not get the response from server.')

page_content = response.text

book_page_link_patt = re.compile(r'<div class="feat-img">\s*<a href="(.*?)">')
book_page_links = re.findall(book_page_link_patt, page_content)

book_image_link_patt = re.compile(r'<div class="feat-img">\s*<a href=".*?">\s*<img width="\d*"? height="\d*"? src="(.*?)"')
book_image_links = re.findall(book_image_link_patt, page_content)

book_name_patt = re.compile(r'<header>\s*<a href=".*?" class="title">(.*?)</a>')
book_names = re.findall(book_name_patt, page_content)


length = len(book_names)
create_dir('dimik_pub')
loc = os.getcwd()
os.chdir(os.path.join(loc, 'dimik_pub'))
for book_index in range(length):
    book_folder_name = re.search(r'book/(\d*)/(.*)', book_page_links[book_index]).groups()
    book_folder_name = book_folder_name[0] + '_' + book_folder_name[1].replace('-', '_')

    create_dir(book_folder_name)
    # os.chdir(os.path.join(os.getcwd(), book_folder_name))
    os.chdir(os.path.join(os.getcwd(), book_folder_name))
    with open(os.path.join(os.getcwd(), 'info.txt'), 'a', encoding='utf-8') as file:
        file.write('Name: %s \n' % book_names[book_index])
        file.write('Link: %s \n' % book_page_links[book_index])
        file.write('Image: %s \n' % book_image_links[book_index])
    os.chdir('..\\')



