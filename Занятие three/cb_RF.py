import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"

responce = requests.get(url)
soup = BeautifulSoup(responce.content, features="xml")


def get_course(course_id):
    return soup.find("Valute", ID="R01235", ).Value.text
    return soup.find("Valute", ID="R01239", ).Value.text
    return soup.find("Valute", ID="R01375", ).Value.text




