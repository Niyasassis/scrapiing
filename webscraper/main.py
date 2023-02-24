import requests
import pandas as pd
from bs4 import BeautifulSoup



url = "https://quotes.toscrape.com"




page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.content,'lxml')



quotes = soup.find_all('div',{"class":"quote"})

quote_file =[]

for t in quotes:
    text = t.find('span',class_="text").text
    author = t.find('small',class_="author").text
    code = t.find('a')
    autherLink = url+code["href"]

    # append detils to file

    quote_file.append([text,author,autherLink])
    

df= pd.DataFrame(quote_file)
df.to_csv('quotes.csv',index=False, header=["Quotes",'Author',"Author Link"])



