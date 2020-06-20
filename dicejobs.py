import requests
import webbrowser
from bs4 import BeautifulSoup
import re
import os
import dominate
from dominate.tags import title,div,a,h1,attr,link,p,h2
from dominate import document

#Dice job search
#position = input('Position?: ')
position = 'DevOps'
dice_url = 'https://www.dice.com/jobs?q=' + position + '&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en'

session = requests.Session()
r = session.get(dice_url)
soup = BeautifulSoup(r.text, 'html.parser')
links =  soup.find_all('a', class_='dice-btn-link loggedInVisited easy-apply')
linksap =  soup.find_all('a', class_='dice-btn-link loggedInVisited')
linksapz = list(links + linksap)
linkopen = min(75, len(linksapz))
f = open('dice_jobs.csv','w')
for i in range(linkopen):
    urlopen = 'http://www.dice.com' + str(linksapz[i].get('href')) + ' ' + '\n'
    f.write(urlopen)
    f.close

f = open('dice_jobs.csv', 'r')

doc = dominate.document(title='Tech Jobs')

with doc.head:
    link(rel='stylesheet', href='jobs.css')

with doc:
    h1('New' + ' ' + position + ' ' + 'Jobs')
    with div():
        h2('Dice' + ' ' + position + ' ' + 'Jobs')
        attr(cls='body')
        for path in f:
            a(position, href=path)

with open('joblinks_dice.html', 'w') as f4:
    f4.write(str(doc))
f4.close()

webbrowser.open('C:/Jobs/joblinks_dice.html')