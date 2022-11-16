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


# webdriver 
url = 'https://hair-chiba.or.jp/salon/11510/'
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)



# find the table with all the data 
table = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/table')
tr_name = table.find_element(By.XPATH, 'tbody/tr[1]/td[2]')
# tr_address =
# tr_tel =
# tr_hours =
# tr_closed =
# tr_hp = 
# tr_email = 
print(tr_name.text)

# Empty list for the 7 'tr's
tr1 = []
tr2 = []
tr3 = []
tr4 = []
tr5 = []
tr6 = []
tr7 = []







# pandas dictionary 
dict = {'店 名': tr1, '住所': tr2, 'TEL': tr3, '営業時間': tr4, '定休日': tr5, 'HP': tr6, 'Email': tr7}
df = pd.DataFrame(dict)

df.to_csv(output_csv)
print(df)