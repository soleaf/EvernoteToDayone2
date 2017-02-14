# -*- coding: utf-8 -*-
"""
Move notes from Evernote to DayOne2 on Mac
ILHO AHN (soleaf@gmail.com)
----
PROCEDURE
1 ) Open Evernote and select notes for export.
2 ) Right click and click 'Export Note...' to call 'Export Selected Notes' window.
3 ) Change Format to 'HTML' and save anywhere
4 ) To install DayOne2 CLI run 'sudo /Applications/Day\ One.app/Contents/Resources/install_cli.sh' on Terminal
5 ) Run 'python evernotehtml_to_dayone.py' on Terminal app
    If you get some error for not found library 'BeautifulSoup', run 'pip install BeautifulSoup'
"""

import os
import urllib
import sys
import BeautifulSoup
from subprocess import call


# Decode image path
def decode_img_path(img_path):
    return '%s/%s' % (evernote_html_path, urllib.unquote((str(img_path))))


# parse html to dict
def read_html(html_path):
    with open(html_path, 'r') as html_file:
        html = html_file.read()
        soup = BeautifulSoup.BeautifulSoup(html)
        texts = soup.find('body').findAll(text=True)
        doc = {'date': soup.find('meta', {'name': 'created'})['content'],
               'img': map(lambda x: decode_img_path(x['src']), soup.findAll('img')),
               'text': '\n'.join(texts)
               }
        return doc


# insert to dayone using dayone2 cli
def insert_dayone(doc):
    command = ['dayone2', 'new', doc['text'], '-d', doc['date']]
    # journal = doc['date'].split('-')[0]
    # command.extend(['-j', journal])
    if len(doc['img']):
        command.append('-p')
        for img in doc['img']:
            command.append(img)
    print command
    print call(command)

# Exported evernote html path
evernote_html_path = sys.argv[1]
print 'target path : %s' % evernote_html_path

for html_path in os.listdir(evernote_html_path):

    # Onely .html file and except index.html file
    if html_path.find('.html') < 0 or html_path == 'index.html':
        continue

    # Parsing
    parsed_doc = read_html('%s/%s' % (evernote_html_path, html_path))
    print parsed_doc

    # Insert
    insert_dayone(parsed_doc)

print 'END JOB'
