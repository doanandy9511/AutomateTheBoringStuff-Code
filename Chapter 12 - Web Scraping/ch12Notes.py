# Chapter 12 - Web Scraping notes
# notes from https://automatetheboringstuff.com/2e/chapter12/
# all credit goes to Al Sweigart

#%% Web scraping is the term for using a program to download and process content from the web
#webbrowser Comes with Python and opens a browser to a specific page.
#requests Downloads files and web pages from the internet.
#bs4 Parses HTML, the format that web pages are written in.
#selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.
import webbrowser
webbrowser.open('https://inventwithpython.com')
# mapIt.py

# %% Downloading files from the web w the requests module
import requests
# %% Downloading a web page w the requests.get() fn
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
# requests.models.Response
res.status_code == requests.codes.ok
# True
len(res.text)
# 178978
print(res.text[:250])
'''
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Projec
'''
# %% Checking for errors
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
# HTTPError: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist
# %%
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
# There was a problem: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist

# note: Always call raise_for_status() after calling requests.get().
# You want to be sure that the download has actually worked before your program continues.

# %% Saving downloaded files to the hard drive
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
with open('RomeoAndJuliet.txt', 'wb') as playFile:# write binary mode
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
# each chunk is of the bytes data type
# 100,000 bytes is generally good size
'''
To review, here’s the complete process for downloading and saving a file:

1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
5. Call close() to close the file.
'''

# %% HTML
# Hypertext Markup Language (HTML) is the format 
# that web pages are written in
# Resources for learning HTML
'''
https://developer.mozilla.org/en-US/learn/html/
https://htmldog.com/guides/html/beginner/
https://www.codecademy.com/learn/learn-html
'''