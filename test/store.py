# https://stackoverflow.com/questions/33633416/convert-html-table-to-csv-in-python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os, time, datetime
import csv


# output file name 
output_csv = 'store.csv'

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
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)


# find the table with all the data 
table = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/table')

with open (output_csv, 'w', newline='') as csv_file:
    wr = csv.writer(csv_file)
    for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
        wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])


#print elapsed time
end = time.time()
elapsed = end - start
print('Task Completed in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)) + '\n')