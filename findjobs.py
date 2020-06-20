import requests
import webbrowser
from bs4 import BeautifulSoup
import re
import os
import dominate
from dominate.tags import title,div,a,h1,attr,link,p,h2
from dominate import document

#Dice job search
position = input('Positions?: ')
#position = 'Data Analyst'
dice_url = 'https://www.dice.com/jobs?q=' + position + '&l=Miami%2C+FL'

session = requests.Session()
r = session.get(dice_url)
soup = BeautifulSoup(r.text, 'html.parser')
links =  soup.find_all('a', class_='dice-btn-link loggedInVisited easy-apply')
linksap =  soup.find_all('a', class_='dice-btn-link loggedInVisited')
linksapz = list(links + linksap)
linkopen = min(30, len(linksapz))
f = open('dice_jobs.csv','w')
for i in range(linkopen):
    urlopen = 'http://www.dice.com' + str(linksapz[i].get('href')) + ' ' + '\n'
    f.write(urlopen)
    f.close

#CareerBuilder
cb_url = 'https://www.careerbuilder.com/jobs-' + position + '-in-miami,fl?sort=date_desc'

session = requests.Session()
r = session.get(cb_url)
soup = BeautifulSoup(r.text, 'html.parser')
links =  soup.find_all(href=re.compile('/job/'))
true_links = list(set(links))
linkopen = min(30, len(true_links))
f2 = open('cb_jobs.csv','w')
for i in range(linkopen):
    urlopen = 'http://www.careerbuilder.com/' + str(true_links[i].get('href')) + ' ' + '\n'
    f2.write(urlopen)
    f2.close

#monster
monster_url = 'https://www.monster.com/jobs/search/?q=' + position + '&where=Miami__2C-FL&intcid=skr_navigation_nhpso_searchMain&jobid=195461048'

session = requests.Session()
r = session.get(monster_url)
soup = BeautifulSoup(r.text, 'html.parser')
links =  soup.find_all(href=re.compile('https://job-openings.monster.com/'))
true_links = list(set(links))
linkopen = min(30, len(true_links))
f3 = open('monster_jobs.csv', 'w')
for i in range(linkopen):
    urlopen = str(true_links[i].get('href')) + '\n'
    f3.write(urlopen)
    f3.close

f = open('dice_jobs.csv', 'r')
f2 = open('cb_jobs.csv', 'r')
f3 = open('monster_jobs.csv', 'r')

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
    with div():
        h2('Career Builder' + ' ' + position + ' ' + 'Jobs')
        attr(cls='body')
        for path2 in f2:
            a(position, href=path2)
    with div():
        h2('Monster' + ' ' + position + ' ' + 'Jobs')
        attr(cls='body')
        for path3 in f3:
            a(position, href=path3)

with open('joblinks.html', 'w') as f4:
    f4.write(str(doc))
f4.close()

webbrowser.open('C:/Jobs/joblinks.html')
