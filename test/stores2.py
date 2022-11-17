from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import os, time, datetime


# output file name 
output_csv = 'stores22222.csv'

# start timer 
start = time.time()
# timestamp
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()


fakelist = ['https://hair-chiba.or.jp/salon/11510/', 'https://hair-chiba.or.jp/salon/1102346/','https://hair-chiba.or.jp/salon/10101/']


# pandas dictionary 
dict = {'店名': [], '住所': [], 'TEL': [], '営業時間': [], '定休日': [], 'HP': [], 'Email': []}

for i in fakelist:

    # webdriver 
    url = i
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)


    # find the table with all the data 
    table = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/table')
    
    tr1 = table.find_element(By.XPATH, 'tbody/tr[1]/td[2]').text
    tr2 = table.find_element(By.XPATH, 'tbody/tr[2]/td[2]').text
    tr3 = table.find_element(By.XPATH, 'tbody/tr[3]/td[2]').text
    tr4 = table.find_element(By.XPATH, 'tbody/tr[4]/td[2]').text
    tr5 = table.find_element(By.XPATH, 'tbody/tr[5]/td[2]').text
    tr6 = table.find_element(By.XPATH, 'tbody/tr[6]/td[2]').text
    tr7 = table.find_element(By.XPATH, 'tbody/tr[7]/td[2]').text

    dict['店名'].append(tr1)
    dict['住所'].append(tr2)
    dict['TEL'].append(tr3)
    dict['営業時間'].append(tr4)
    dict['定休日'].append(tr5)
    dict['HP'].append(tr6)
    dict['Email'].append(tr7)



df = pd.DataFrame(dict)

df.to_csv(output_csv)
print(df)