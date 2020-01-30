from lxml.html import fromstring
from bs4 import BeautifulSoup
import download
import pandas as pd

excel_file = input('Type the file name: ')
url_data = pd.read_excel(excel_file)
print("File successfully  DOWNLOADED")
column_name = input('Type the column name: ')
url_data_list = url_data[column_name].tolist()

url_list = ['https://anketa.alfabank.ru/land/land6/step1?platformId=Yandex_RTB_Banner_CPM_indoor_AlfaBank_KK_100days_August-September19_OMD_restorany_&utm_source=Yandex_RTB&utm_medium=Banner_CPM_indoor&utm_campaign=AlfaBank_KK_100days_August-September19_OMD&utm_term=&utm_content=restorany',
             'https://wcm-ru.frontend.weborama.fr/fcgi-bin/dispatch.fcgi?a.A=cl&a.si=4980&a.te=1098&a.aap=570&a.agi=289&g.lu=',
             'https://rko.tochka.com/musicians?referer1=rk_yandex_musicians&utm_medium=cpm&utm_source=rk_yandex&utm_campaign=music&utm_term=inters&utm_content=music',
             'https://pay.visa.ru/?utm_source=Yandex_cpm_55&utm_medium=Banner&utm_term=73451_Magnit_KV&utm_campaign=EDS_Feb_Mar66']

categories = ["АКЦИЯ","ВИРТ_ЖИЛАЯ НЕДВИЖИМОСТЬ И ИПОТЕКА", "ДЕБЕТОВЫЕ КАРТЫ",
              "ЗАЙМЫ", "ИМИДЖЕВОЕ РАЗМЕЩЕНИЕ", "ИПОТЕЧНОЕ КРЕДИТОВАНИЕ",
              "КАРТЫ РАССРОЧКИ", "КАСКО", "КРЕДИТНЫЕ КАРТЫ", "ЛИЗИНГ",
              "МОБИЛЬНАЯ СВЯЗЬ", "ОСАГО", "ПОТРЕБИТЕЛЬСКОЕ КРЕДИТОВАНИЕ",
              "РКО", "СТРАХОВАНИЕ ВКЛАДОВ", "СТРАХОВАНИЕ ВЫЕЗЖАЮЩИХ ЗА РУБЕЖ",
              "УСЛУГИ ПАРИКМАХЕРСКИХ И КОСМЕТИЧЕСКИХ САЛОНОВ", "CASHBACK",
              "КРЕДИТ ДЛЯ БИЗНЕСА", "ИНВЕСТИЦИИ", "ОБРАЗОВАНИЕ",
              "СТРАХОВАНИЕ ОТ НЕСЧАСТНОГО СЛУЧАЯ", "СТРАХОВАНИЕ",
              "ДЕНЕЖНЫЕ ПЕРЕВОДЫ", "ВАКАНСИИ", "АВТОКРЕДИТОВАНИЕ",
              "ПЕНСИОННЫЕ НАКОПЛЕНИЯ", "МОБИЛЬНОЕ ПРИЛОЖЕНИЕ",
              "ПЕРСОНАЛЬНОЕ ОБСЛУЖИВАНИЕ", "ВКЛАДЫ", "ЕДА"]

regex = [["акц"], ["ипотек"], ["дебет"], ["займ"], ["имиджев"], ["ипотеч"], ["рассрочк"], ["каско"], ["кредитн"],
         ["лизинг"], ["мобильн"], ["осаго"], ["потребит"], ["рко"], ["страхов"], ["страхование"], ["салон"],
         ["cashback"], ["бизнес"], ["инвест"], ["образован"], ["несчастн"], ["страхование"], ["перевод",
         "visa", "mastercard"], ["ваканс"], ["автокред"], ["пенсион"], ["приложен"], ["обслуж"], ["вклад"], ["еда"]]

result = []

print ("""MENU:
1. BeautifulSoup method,
2. lxml method.""")

opt = int(input("Choose method --> "))

if opt == 1:
    for url in url_list:
        html = download.download(url)
        soup = BeautifulSoup(html, 'html5lib')
        head = soup.find('head')
        title = head.find('title')
        tit_name = title.text
        for reg in regex:
            if reg in tit_name.lower(): 
                result.append(categories[regex.index(reg)])
                break
        if url_list.index(url)+1 > len(result):
            result.append("Not matches")

elif opt == 2:
    for url in url_list:
        html = download.download(url)
        tree = fromstring(html)
        title = tree.cssselect('head > title')[0]
        cont = title.text_content()
        for elemnt in regex:
            for reg in elemnt:
                if reg in cont.lower():
                    result.append(categories[regex.index(elemnt)])
                    break
        if url_list.index(url)+1 > len(result):
            result.append("Not matches")

print (result)
url_data['Result'] = result
url_data.to_excel('output.xlsx')
