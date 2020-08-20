import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()

soup = bs.BeautifulSoup(sauce, 'xml')
for url in soup.find_all('loc'):
    print(url.text)

##########################################################################################
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# table = soup.table
table = soup.find('table')

table_rows = table.find_all('tr')  # tr = table row

for tr in table_rows:
    td = tr.find_all('td')  # td = table data
    row = [i.text for i in td]
    print(row)

##########################################################################################
# same thing but using pandas to get DataFrames
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
for df in dfs:
    print(df)
