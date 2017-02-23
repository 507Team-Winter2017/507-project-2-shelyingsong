#proj2.py
import urllib.request
import requests
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
times_url = 'http://nytimes.com'
fhand = urllib.request.urlopen(times_url)
soup = BeautifulSoup(fhand, 'html.parser')
for i,times_heading in enumerate(soup.find_all(class_ ="story-heading")):
    if i < 10:
       if times_heading.a:
          print(times_heading.a.text.replace("\n", " ").strip())
       else:
          print(story_heading.contents[0].strip())
### Your Problem 1 solution goes here


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')
michigandaily_url = 'https://www.michigandaily.com/'
michigandaily = urllib.request.urlopen(michigandaily_url)
michigandaily_soup = BeautifulSoup(michigandaily,'html.parser')
for most_read in michigandaily_soup.find('div', class_="panel-pane pane-mostread").find_all('li'):
	if most_read.a:
		print(most_read.a.text.replace("\n"," ").strip())
	else:
	    print(most_read.contents[0].strip())	

### Your Problem 2 solution goes here


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")
gallery_url = 'http://newmantaylor.com/gallery.html'
gallery = urllib.request.urlopen(gallery_url)
gallery_soup = BeautifulSoup(gallery, 'html.parser')
for gallery_img in gallery_soup.find_all('img'):
     if gallery_img.get('alt', ' ') != ' ':
        print(gallery_img.get('alt', ' '))
     else:
        print('No alternative text provided!!')

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
def umsiEmail(x, count):
    req = urllib.request.Request(x, None, {'User-Agent': 'SI_CLASS'})
    umsi = urllib.request.urlopen(req)
    umsi_soup = BeautifulSoup(umsi,'html.parser')
    for umsi_email in umsi_soup.find_all('div', class_="field field-name-contact-details field-type-ds field-label-hidden"):
        umsi_email = umsi_email.find('a')
        email_url = 'https://www.si.umich.edu/' + umsi_email.get('href', None)
        reqs = urllib.request.Request(email_url, None, {'User-Agent': 'SI_CLASS'})
        emails = urllib.request.urlopen(reqs)
        email_soup  = BeautifulSoup(emails, 'html.parser')
        email = email_soup.find('div', class_="field field-name-field-person-email field-type-email field-label-inline clearfix").find('a')
        print(str(count) + ' ' + email.get_text())
        count = count + 1
    if len(umsi_soup.find(class_="pager-next last")) > 0:
       for nextpage in umsi_soup.find(class_="pager-next last").find_all('a'):
           nextPage_url = 'https://www.si.umich.edu/' + nextpage.get('href', None)
           umsiEmail(nextPage_url, count)
original_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
umsiEmail(original_url, 1)	   	   

### Your Problem 4 solution goes here
