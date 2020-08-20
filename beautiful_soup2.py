import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav
# print(nav)

# for url in nav.find_all('a'):
#     print(url.get('href'))
#
# body = soup.body
# for paragraph in body.find_all('p'):
#     # this in line before is for paragraph in body.findall()....it is not gonna find stuff that is not in <p>
#     print(paragraph.text)

for div in soup.find_all('div', class_='body'):  # this is finding all of the text that is between <div>
    print(div.text)
