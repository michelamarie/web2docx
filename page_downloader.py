# Download an entire web page, with some exclusions

import urllib.request, urllib.error, urllib.parse
import pypandoc
import os


# TODO: Make script read taget sites from input file.

# Open the desired webpage
url = 'https://ionica.ca/'
response = urllib.request.urlopen(url)
webContent = response.read()

# Save the page to local disk
f = open('ionica.html','wb')
f.write(webContent)
f.close()

output = pypandoc.convert_file('ionica.html', 'docx', outputfile = 'ionica.docx')

# TODO: Remove downloaded HTML files after conversions.
# TODO: Add exceptions for missing input files or invalid entries in input files.

