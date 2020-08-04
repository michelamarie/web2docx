from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
import pypandoc


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

# Launch browser
browser = webdriver.Firefox()
#browser.implicitly_wait(4)

# Get the authentication page
browser.get('https://cas.id.ubc.ca/ubc-cas/login')

# Find credential fields and send keystrokes to them
user_name_field = browser.find_element_by_name("username")
password_field = browser.find_element_by_name("password")
user_name_field.send_keys(user_name_input)
password_field.send_keys(password_input)
time.sleep(1)
password_field.send_keys(Keys.RETURN)

time.sleep(2)

# Get a first sample page. We do this because there is a delay of a few seconds before the first page loads after authenticating.
browser.get('https://blogs.ubc.ca/ubcworkdayjobaids/archives/1409')

time.sleep(4)

url_file = open("urls-all.txt", "r")
url_list = url_file.readlines()

for line in url_list:
    # Fetch a page, then wait for it to load
    browser.get(line)
    time.sleep(2)
    # Store the page title in a variable
    article_title = browser.title
    # Select the element by its HTML tag
    contents = browser.find_element_by_tag_name('article')
    # Set only the source code inside the 'article' tags in a variable
    article_content = contents.get_attribute('innerHTML')
    # Save selected source code in an HTML file
    with open("./documents/"+ article_title +".html", "w") as f:
        f.write(article_content)
    # Convert saved HTML file to a separate docx file.
    output = pypandoc.convert_file("./documents/"+ article_title +'.html', 'docx', outputfile = "./documents/"+ article_title +'.docx')
    time.sleep(0)

time.sleep(0)
os.system('/bin/mv documents/*.html documents/temp/')

# TODO: Consider catching exceptions for bad URLs in input file.