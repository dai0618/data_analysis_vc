import re
import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.jpx.co.jp/listing/stocks/new/index.html"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser", from_encoding="utf-8")

company_name_list = []
company_link_list = []

def find_data(web_url):
    for i, bs4_data in enumerate(soup.find_all("tr")):
        if i % 2 == 0 and i != 0:
            #会社名の取得。データの取得から改行コードやコメ印空白の置換を行っている。
            company_name = re.sub("\n|\r|代表者インタビュー", "", bs4_data("td")[1].text)
            company_name = company_name.replace(" ","")
            company_name = company_name.replace("*","")
            company_name_list.append(company_name)
            

        elif i % 2 == 1 and i != 1:
            #urlのリンクを取得。
            company_link = "https://www.jpx.co.jp" + bs4_data("td")[1]("a")[0]['href']
            company_link_list.append(company_link)

def download_pdf():
    #会社名をファイル名にしてpdfファイルをダウンロード
    for name, link in zip(company_name_list, company_link_list):
        urllib.request.urlretrieve(link,f"./data_folder/{name}.pdf")

if __name__ == "__main__":
    find_data(url)
    download_pdf()
