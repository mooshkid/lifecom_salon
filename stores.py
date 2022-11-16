from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import os, time, datetime


# output file name 
output_csv = 'stores.csv'

# start timer 
start = time.time()
# timestamp
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()


fakelist = ['https://hair-chiba.or.jp/salon/11510/', 'https://hair-chiba.or.jp/salon/1102346/']
# Empty list for the 7 'tr's
tr1 = []
tr2 = []
tr3 = []
tr4 = []
tr5 = []
tr6 = []
tr7 = []

for i in fakelist:

    # webdriver 
    url = i
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)


    # find the table with all the data 
    table = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/table')
    tr_name = table.find_element(By.XPATH, 'tbody/tr[1]/td[2]').text
    tr_address = table.find_element(By.XPATH, 'tbody/tr[2]/td[2]').text
    tr_tel = table.find_element(By.XPATH, 'tbody/tr[3]/td[2]').text
    tr_hours = table.find_element(By.XPATH, 'tbody/tr[4]/td[2]').text
    tr_closed = table.find_element(By.XPATH, 'tbody/tr[5]/td[2]').text
    tr_hp = table.find_element(By.XPATH, 'tbody/tr[6]/td[2]').text
    tr_email = table.find_element(By.XPATH, 'tbody/tr[7]/td[2]').text

    tr1.append(tr_name)
    tr2.append(tr_address)
    tr3.append(tr_tel)
    tr4.append(tr_hours)
    tr5.append(tr_closed)
    tr6.append(tr_hp)
    tr7.append(tr_email)


# pandas dictionary 
dict = {'店名': tr1, '住所': tr2, 'TEL': tr3, '営業時間': tr4, '定休日': tr5, 'HP': tr6, 'Email': tr7}
df = pd.DataFrame(dict)

df.to_csv(output_csv)
print(df)