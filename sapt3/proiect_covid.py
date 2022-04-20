from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
link = BeautifulSoup(r.text, "html.parser")
# print(link)

title = link.find_all('table', attrs={'width':'710'})
# print(title)
header = []
dataset = []
for i in title:
    for tbody in i.find_all('tbody'):
            td_list = []
            for tr_index in tbody.find_all('tr'):
                if tr_index.find_all('td'):
                    header = [td_index.get_text() for td_index in tr_index.find_all('td')]
                    dataset.append(header)
                    # print(header)
# print(dataset)

df = pd.DataFrame(dataset)
df.to_csv("covid.xls")