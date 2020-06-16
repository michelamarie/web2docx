# Download an entire web page, with some exclusions
# By Michela Toscano

import requests
from requests.auth import HTTPDigestAuth
import pypandoc
import os


# Get authorisation credentials from user

print('')
print('Hello! Please enter your user name.')
user_name_input = input()
print('')
print('Excellent! Now please enter your password.')
password_input = input()
print('')
print('Thank you!')
print('')

# Log-in page
login_url = 'https://cas.id.ubc.ca/ubc-cas/login'

# Pages to download
url = 'https://blogs.ubc.ca/ubcworkdayjobaids/archives/1409'

# Hold the credentials for use by the session
credentials = {
    'username': user_name_input,
    'password': password_input
}

# Then we use 's.*' in place of 'requests.*' to invoke the Requests module below.

# Actually authenticate, hold cookies for a session, then download pages
with requests.Session() as session:
    post = session.post(login_url, data = credentials)
    web_page = session.get(url)
    #print(web_page.content)
    with open ('1409.html', 'wb') as f:
        f.write(web_page.content)


# TODO: Make script read taget sites from input file.

# TODO: Use Python or awk to pull article names and numbers and use them to name the output files.


output = pypandoc.convert_file('1409.html', 'docx', outputfile = '1409.docx')

# TODO: Remove downloaded HTML files and temporary files after conversions.
# TODO: Add exceptions for missing input files or invalid entries in input files.